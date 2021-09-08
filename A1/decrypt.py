import numpy as np
import re
from sympy import Matrix
import utils

encryptedText = utils.getTextFromFile('encryptedText.txt')
key = utils.geteKeyFromFile('key.txt')
n = np.shape(key)[0]
print("Key Size:",n)

decryptedText = (utils.decryption(encryptedText,key,n))
print("Decrypted Text: ",decryptedText)