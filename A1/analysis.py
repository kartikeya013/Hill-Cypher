import numpy as np
import utils
import argparse


def analysis(messageFile,encryptedFile):
    message = utils.getTextFromFile(messageFile)
    plainText = utils.process_message(message, 1)
    encryptedText = utils.getTextFromFile(encryptedFile)
    # print(plainText,encryptedText)
    # assert len(plainText)==len(encryptedText)
    keyList = [[] for i in range(11)]
    all_ics = np.zeros(shape=(11,), dtype=np.float32)

    for n in range(2,11):
        key = utils.get_key(plainText,encryptedText,n)
        if (not key is None) and utils.check_invertible(key):
            decryptedText = utils.decryption(encryptedText,key,n)
            ic = utils.index_of_coincidence(decryptedText)
            if abs(ic-0.069) < 10**-2:
                return n,key
        

    # keySize = (min(range(len(all_ics)), key=lambda i: abs(all_ics[i]-0.069)))
    # print('Key Size: ',keySize)
    return None,None
    

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-m','--message', type=str, help='Message filename', required=True)
    parser.add_argument('-e','--encrypted', type=str, help='Encrypted filename', required=True)
    args = vars(parser.parse_args())
    keySize,key = analysis(args['message'],args['encrypted'])

    
    