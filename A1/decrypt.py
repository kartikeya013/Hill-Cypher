import numpy as np
import re
from sympy import Matrix
import utils
import sys
import argparse

def decrypt(encryptedTextFile, keyFile):
    encryptedText = utils.getTextFromFile(encryptedTextFile)
    key = utils.getKeyFromFile(keyFile)
    n = np.shape(key)[0]
    decryptedText = (utils.decryption(encryptedText,key,n))
    return decryptedText

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-e','--encrypted', type=str, help='Encrypted filename', required=True)
    parser.add_argument('-k','--key', type=str, help='Key filename', required=True)
    parser.add_argument('-o','--output', type=str,default='output_decrypted_text.txt', help='Decrypted file name', required=False)
    args = vars(parser.parse_args())
    encryptedText = decrypt(args['encrypted'],args['key'])
    utils.writeFile(args['output'], encryptedText)