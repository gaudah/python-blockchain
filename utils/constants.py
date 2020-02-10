import string

MIN_AMT = 5000
MAX_AMT = 50000
VOWELS = "aeiou"
CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))
RANDOM_LENGTH = 5
GENESIS_BLOCK_DATA = {'sender':'Aishwarya','recipient':'Sapana','amount':17000}
GENESIS_BLOCK_HASH = 'arbitrary'

def trial():
    print("HELLO")