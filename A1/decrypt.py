import numpy as np
import re
from sympy import Matrix


encryptedText = "CDINMUQABF"
key = ([[1,2],[2,3]])
n = np.shape(key)[0]
print("Key Size:",n)

segments = [encryptedText[n*i:n*(i+1)] for i in range(int(len(encryptedText)/n))]
segments = np.array([np.array([ord(x[i])-ord('A') for i in range(len(x))]).T for x in segments]).T
# segments = np.array([ord(c)-ord('A') for c in plainText])
# segments = segments.reshape(n,-1)
print(segments)
print(np.shape(segments))
A = Matrix(key)
A = A.inv_mod(26) 
decrypted = np.matmul(A,segments)%26
print('Decrypted: \n',decrypted)
encrypted = decrypted.ravel(order='F')
# print(encrypted)
decryptedText = list(map(chr,encrypted+ord('A')))
decryptedText = "".join(decryptedText)
print(decryptedText)