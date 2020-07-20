from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='python-blockchain',
    version='1.0',
    author='Aishwarya Gaud',
    author_email='aishwaryagaud17@gmail.com',
    url='https://github.com/gaudah/python-blockchain.git',
    description='Simple bank transaction blockchain from one user to another',
    long_description=readme,
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['requests==2.8.1'],
    #scripts=['python_blockchain/blockchain_bank_transaction.py'],
    entry_points={
	'console_scripts': [
            #'snek = python_sample_project.snek:main',
            #'chain = python_blockchain.blockchain_bank_transaction:main',
        ],
    }
)

