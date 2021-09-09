import numpy as np
import utils
import argparse


def analysis(messageFile,encryptedFile):
    message = utils.getTextFromFile(messageFile)
    plainText = utils.process_message(message, 1)
    encryptedText = utils.getTextFromFile(encryptedFile)
    keyList = [[] for _ in range(11)]
    all_ics = np.zeros(shape=(11,), dtype=np.float32)

    for n in range(2,11):
        print("Checking for key of size",n)
        key = utils.get_key(plainText,encryptedText,n)
        if (not key is None) and utils.check_invertible(key):
            decryptedText = utils.decryption(encryptedText,key,n)
            ic = utils.index_of_coincidence(decryptedText)
            keyList[n] = key
            all_ics[n] = ic
            print("Obtained IC for key of size",n,"is",ic)
            if abs(ic-0.0686) < 10**-2:
                return n,ic,key
        else:
            print('\n')
        

    keySize = (min(range(len(all_ics)), key=lambda i: abs(all_ics[i]-0.0686)))
    return keySize,all_ics[keySize],keyList[keySize]
    

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-m','--message', type=str, help='Message filename', required=True)
    parser.add_argument('-e','--encrypted', type=str, help='Encrypted filename', required=True)
    args = vars(parser.parse_args())
    keySize,ic,key = analysis(args['message'],args['encrypted'])
    print("Key Size:",keySize)
    print("Index of Coincidence:",ic)
    utils.write_key_to_file(key, 'analysis_key.txt')

    
    