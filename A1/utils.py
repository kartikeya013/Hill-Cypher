import numpy as np
from numpy.core.numeric import _rollaxis_dispatcher
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
    det = np.linalg.det(key)    # TODO check what if this is zero
    gcd = np.gcd(int(round(det,2)), alphabet_size)
    return (gcd==1)

def get_text(plain_text, encrypted_text, n):
    print(plain_text,encrypted_text)
    start = 0
    while(start<=len(encrypted_text)-n*n):
        plainText = plain_text[start:start + n*n]
        encryptedText = encrypted_text[start:start + n*n]
        P = [plainText[n*i:n*(i+1)] for i in range(n)]
        P = np.array([np.array([ord(x[i])-ord('A') for i in range(len(x))]).T for x in P]).T
        print("P:\n",P)
        if check_invertible(P):
            C = [encryptedText[n*i:n*(i+1)] for i in range(n)]
            C = np.array([np.array([ord(x[i])-ord('A') for i in range(len(x))]).T for x in C]).T
            print("C:\n",C)
            return C,P
        start += n


def get_key(plainText,encryptedText,n,alphabet_size=26):
    C,P = get_text(plainText,encryptedText,n)
    P_inv = Matrix(P)
    P_inv = P.inv_mod(alphabet_size) 
    key = np.matmul(C,P_inv)%alphabet_size
    print('Key: \n',key)
    # key = key.ravel(order='F')
    return key


print("Hello")

