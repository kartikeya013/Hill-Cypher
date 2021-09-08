from os import utime
import numpy as np
import re
import utils
import sys
import argparse

def encrypt(messageFile, keyFile):
    message = utils.getTextFromFile(messageFile)
    key = utils.getKeyFromFile(keyFile)
    n = np.shape(key)[0]
    assert utils.check_invertible(key)
    plainText = utils.process_message(message, n)
    encryptedText = utils.encryption(plainText,key,n)
    return encryptedText

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-m','--message', type=str, help='Message filename', required=True)
    parser.add_argument('-k','--key', type=str, help='Key filename', required=True)
    parser.add_argument('-o','--output', type=str,default='output_encrypted_text.txt', help='Encrypted file name', required=False)
    args = vars(parser.parse_args())
    encryptedText = encrypt(args['message'],args['key'])
    utils.writeFile(args['output'], encryptedText)