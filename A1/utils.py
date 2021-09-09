import numpy as np
from numpy.core.numeric import _rollaxis_dispatcher
from sympy import Matrix
import re

def getTextFromFile(file):
    text_file = open(file, "r")
    data = text_file.read()
    text_file.close()
    return (data)

def getKeyFromFile(file):
    with open(file) as f:
        n = [int(x) for x in next(f).split()] 
        lines = []
        for line in f:
            lines.append([int(x) for x in line.split()])
    return np.array(lines)

def write_key_to_file(key, file):
    n = key.shape[0]
    with open(file, 'w') as testfile:
        testfile.write(str(n) + '\n')
        for row in key:
            testfile.write(' '.join([str(a) for a in row]) + '\n')
    

def writeFile(file,s):
    with open(file, "w") as f:
        f.write(s)

def index_of_coincidence(s):
    N = len(s)
    freq = [s.count(chr(i+ord('A'))) for i in range(26)]
    ic = ((float)(sum([i*(i-1) for i in freq])))/(float)(N*(N-1))
    return ic

def process_message(message, key_size):
    message = message.upper()
    s = re.sub('[^A-Z]+','',message)
    while(len(s)%key_size != 0): s += 'X'
    return s

def check_invertible(key, alphabet_size=26):
    key = np.array(key, dtype=np.int32)
    det = np.linalg.det(key)    # TODO check what if this is zero
    gcd = np.gcd(int(round(det,2)), alphabet_size)
    return (gcd==1)

def decryption(encryptedText,key,n):
    if not check_invertible(key):
        print("Provided key is not invertible!")
        return ""
    segments = [encryptedText[n*i:n*(i+1)] for i in range(int(len(encryptedText)/n))]
    segments = np.array([np.array([ord(x[i])-ord('A') for i in range(len(x))]).T for x in segments]).T
    A = Matrix(key)
    A = A.inv_mod(26) 
    decrypted = np.matmul(A,segments)%26
    encrypted = decrypted.ravel(order='F')
    decryptedText = list(map(chr,encrypted+ord('A')))
    decryptedText = "".join(decryptedText)
    return (decryptedText)

def encryption(plainText,key,n):
    segments = [plainText[n*i:n*(i+1)] for i in range(int(len(plainText)/n))]
    segments = np.array([np.array([ord(x[i])-ord('A') for i in range(len(x))]).T for x in segments]).T
    encrypted = np.matmul(key,segments)%26
    encrypted = encrypted.ravel(order='F')
    encryptedText = list(map(chr,encrypted+ord('A')))
    encryptedText = "".join(encryptedText)
    return encryptedText


def get_text(plain_text, encrypted_text, n):
    start = 0
    while(start<=len(plain_text)-n*n):
        plainText = plain_text[start:start + n*n]
        encryptedText = encrypted_text[start:start + n*n]
        P = [plainText[n*i:n*(i+1)] for i in range(n)]
        P = np.array([np.array([ord(x[i])-ord('A') for i in range(len(x))]).T for x in P]).T
        if check_invertible(P):
            C = [encryptedText[n*i:n*(i+1)] for i in range(n)]
            C = np.array([np.array([ord(x[i])-ord('A') for i in range(len(x))]).T for x in C]).T
            return C,P
        else:
            print(f"Window of plaintext {start}:{start+n*n} is not invertible, taking next window")
        start += n

    return None,None


def get_key(plainText,encryptedText,n,alphabet_size=26):
    C,P = get_text(plainText,encryptedText,n)
    if C is None:
        return None
    P = Matrix(P)
    P_inv = P.inv_mod(alphabet_size) 
    key = np.matmul(C,P_inv)%alphabet_size
    return key

