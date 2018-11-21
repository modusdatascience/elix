import os
import pandas as pd
from clinvoc.icd9 import ICD9CM 
from clinvoc.code_collections import CodeCollection
from modulecache.invalidators import FileChangeInvalidator
from modulecache.backends import PickleBackend
# from .resources import resources

vocab = ICD9CM(use_decimals=True)

def _construct_icd9_categories(def_column="Enhanced ICD-9-CM"): # args? 
#     df = pd.read_csv(os.path.join(resources, 'NDF_January_2016.xlsx'))
    df = pd.read_csv("/Users/Matt/Work/elix/elix/resources/elixhauser_definitions.csv")
    elix_cats = {}
    for _, row in df.iterrows():
        category = row['Category']
        codes = row[def_column]
        parsed_codes = vocab.parse(codes)
        elix_cats[(category, vocab.vocab_name, vocab.vocab_domain)] = parsed_codes
        
    return elix_cats
        
    
cache_filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'elix_icd9_cache.pkl')
suppress = globals().keys()
with PickleBackend(cache_filename, suppress) as cache, FileChangeInvalidator(cache, os.path.abspath(__file__)):
    code_set = CodeCollection(*_construct_icd9_categories().items(), name='elix_icd9')