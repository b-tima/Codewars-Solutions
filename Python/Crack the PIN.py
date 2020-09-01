from hashlib import md5
from math import log10, floor

def crack(hash):
    for i in range(1, 100000):
        padded_string = "{}{}".format(''.join('0' for i in range(4-floor(log10(i)))), i)
        if md5(padded_string.encode()).hexdigest() == hash:
            return padded_string
    return "00000"