from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'pysupplychaindemo',
  packages = ['pysupplychaindemo'],
  version = '0.1',
  license = 'Apache',
  description = 'Python Supply Chain Security Demo',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Amirali Sanatinia',
  author_email = 'amirali@ccs.neu.edu',
  url = 'https://github.com/amiralis/python_supply_chain_security_demo',
  install_requires=[
        'requests==2.1.0',
        'flask',
        'urllib3==1.26.5',
        'xml2dict==0.2.2'],
  keywords = ['demo', 'security', 'supply chain'],
  classifiers = [
    	'License :: OSI Approved :: Apache Software License',
    	'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
		],
)