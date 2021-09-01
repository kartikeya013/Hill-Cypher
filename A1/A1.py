import numpy as np
import re

message = "AB CD EEE GH"
key = ([[1,2],[2,3]])
n = np.shape(key)[0]
print("Key Size:",n)
def processMessage(m, n):
    s = re.sub('[^A-Z]+','',m)
    while(len(s)%n != 0): s += 'X'
    return s

plainText = processMessage(message, n)
print('Plain Text:',plainText)

segments = [plainText[n*i:n*(i+1)] for i in range(int(len(plainText)/n))]
segments = np.array([np.array([ord(x[i])-ord('A') for i in range(len(x))]).T for x in segments]).T
# segments = np.array([ord(c)-ord('A') for c in plainText])
# segments = segments.reshape(n,-1)
print(segments)
print(np.shape(segments))
encrypted = np.matmul(key,segments)%26
print('Encrypted: \n',encrypted)
encrypted = encrypted.ravel(order='F')
# print(encrypted)
encryptedText = list(map(chr,encrypted+ord('A')))
encryptedText = "".join(encryptedText)
print(encryptedText)