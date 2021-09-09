import numpy as np
import utils
from decrypt import decrypt
from encrypt import encrypt
from analysis import analysis
import random
from tqdm import tqdm

TESTCASES = 200
MESSAGEFILE = 'input_message.txt'
KEYFILE = 'input_key.txt'
ENCRYPTEDFILE = 'input_encrypted.txt'
message = utils.getTextFromFile(MESSAGEFILE)

for tc in tqdm(range(TESTCASES)):
    key_size = random.randint(2,10)
    # key_size = 10
    processed_message = utils.process_message(message, key_size)
    key = np.random.randint(25, size=(key_size,key_size))
    while not utils.check_invertible(key):
        key = np.random.randint(25, size=(key_size,key_size))
    utils.write_key_to_file(key, 'input_key.txt')
    
    encryptedText = encrypt(MESSAGEFILE,KEYFILE)
    utils.writeFile(ENCRYPTEDFILE, encryptedText)
    decryptedText = decrypt(ENCRYPTEDFILE,KEYFILE)
    if decryptedText != processed_message:
        print("Decryption not matched")
        break
        
    keySize,key_c = analysis(MESSAGEFILE,ENCRYPTEDFILE)
    # print(keySize,key_c)
    if keySize == None or keySize != key_size:
        print("Key Size not matched")
        break

    # if np.array(key_c) != key:
    #     print("Key not matched")
    #     break



# for key_size in range(2,11):    
#     # key_size = 10
#     processed_message = utils.process_message(message, key_size)
#     key = np.random.randint(25, size=(key_size,key_size))
#     while not utils.check_invertible(key):
#         key = np.random.randint(25, size=(key_size,key_size))
#     utils.write_key_to_file(key, 'input_key'+str(key_size)+'.txt')
    
#     encryptedText = encrypt(MESSAGEFILE,'input_key'+str(key_size)+'.txt')
#     utils.writeFile(ENCRYPTEDFILE, encryptedText)
#     decryptedText = decrypt(ENCRYPTEDFILE,'input_key'+str(key_size)+'.txt')
#     if decryptedText != processed_message:
#         print("Decryption not matched")
#         break
        
#     keySize,key_c = analysis(MESSAGEFILE,ENCRYPTEDFILE)
#     # print(keySize,key_c)
#     if keySize == None or keySize != key_size:
#         print("Key Size not matched")
#         break

#     # if np.array(key_c) != key:
#     #     print("Key not matched")
#     #     break




print("Passed")