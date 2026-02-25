'''This is the module for calculation of entropy or uncertainity'''

import string
import math

def check_possibilities(passcode):
    '''Update the character pool according 
        to the charcter set used in passcode
    '''
    character_pool = 0
    if any(c.islower() for c in passcode):
        character_pool +=26
    if any(c.isupper() for c in passcode):
        character_pool +=26
    if any(c.isdigit() for c in passcode):
        character_pool += 10
    if any(c in string.punctuation for c in passcode):
        character_pool +=32
    return character_pool

def caculate_entropy(password):
    '''This function calculates the entropy and returns it'''
    length = len(password)
    charset_size = check_possibilities(password)
    if charset_size == 0:
        return 0
    entropy = length  * math.log2(charset_size)
    return round(entropy,2)
