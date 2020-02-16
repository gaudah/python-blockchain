import constants
import random

"""
    @params : String length
    @description : Generate random string of given length
"""
def generate_string(length):
    word = ""
    for i in range(length):
        if i % 2 == 0:
            word += random.choice(constants.CONSONANTS)
        else:
            word += random.choice(constants.VOWELS)
    return word