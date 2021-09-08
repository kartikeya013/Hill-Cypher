import numpy as np
from sympy import Matrix
import re

def index_of_coincidence(s):
    N = len(s)
    freq = [s.count(chr(i+ord('A'))) for i in range(26)]
    ic = ((float)(sum([i*(i-1) for i in freq])))/(float)(N*(N-1))
    return ic

def process_message(message, key_size):
    s = re.sub('[^A-Z]+','',message)
    while(len(s)%key_size != 0): s += 'X'
    return s

def check_invertible(key, alphabet_size=26):
    key = np.array(key, dtype=np.int32)
    det = np.linalg.det(key)
    gcd = np.gcd(det, alphabet_size)
    return (gcd==1)

print("Hello")

