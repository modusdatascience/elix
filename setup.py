from setuptools import setup, find_packages
import versioneer
setup(name='elix',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      author='Matt Lewis',
      author_email='',
      url='https://github.com/modusdatascience/elix',
      package_data={'elix': ['resources/*']},
      packages=find_packages(),
      requires=['pandas', 'xlrd', 'clinvoc']
     )