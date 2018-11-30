import os
import pandas as pd
from clinvoc.icd10 import ICD10CM 
from clinvoc.code_collections import CodeCollection
from modulecache.invalidators import FileChangeInvalidator
from modulecache.backends import PickleBackend
from .resources import resources

vocab = ICD10CM(use_decimals=True)

def _construct_icd10_categories(def_column="ICD-10"): # args? 
#     df = pd.read_csv(os.path.join(resources, 'NDF_January_2016.xlsx'))
    df = pd.read_csv(pd.read_csv(os.path.join(resources, 'elixhauser_definitions.csv')))
    elix_cats = {}
    for _, row in df.iterrows():
        category = row['Category']
        codes = row[def_column]
        parsed_codes = vocab.parse(codes)
        elix_cats[(category, vocab.vocab_name, vocab.vocab_domain)] = parsed_codes
        
    return elix_cats
        
    
cache_filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'elix_icd10_cache.pkl')
suppress = globals().keys()
with PickleBackend(cache_filename, suppress) as cache, FileChangeInvalidator(cache, os.path.abspath(__file__)):
    code_set = CodeCollection(*_construct_icd10_categories().items(), name='elix_icd10')