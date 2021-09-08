from os import utime
import numpy as np
import re
import utils

# message = "AB CD EEE GH"
message = utils.getTextFromFile('message.txt')
key = utils.geteKeyFromFile('key.txt')
n = np.shape(key)[0]
print("Key Size:",n)
assert utils.check_invertible(key)
plainText = utils.process_message(message, n)
print('Plain Text:',plainText)
utils.writeFile('plainText.txt',plainText)
segments = [plainText[n*i:n*(i+1)] for i in range(int(len(plainText)/n))]
segments = np.array([np.array([ord(x[i])-ord('A') for i in range(len(x))]).T for x in segments]).T
# segments = np.array([ord(c)-ord('A') for c in plainText])
# segments = segments.reshape(n,-1)
print(segments)
print(np.shape(segments))
encrypted = np.matmul(key,segments)%26
encrypted = encrypted.ravel(order='F')
# print(encrypted)
encryptedText = list(map(chr,encrypted+ord('A')))
encryptedText = "".join(encryptedText)
print("Encrypted Text:" ,encryptedText)
utils.writeFile('encryptedText.txt',encryptedText)