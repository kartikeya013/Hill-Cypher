from numpy import dtype, float32
import numpy as np
import utils

plainText = utils.getTextFromFile('plainText.txt')
encryptedText = utils.getTextFromFile('encryptedText.txt')

assert len(plainText)==len(encryptedText)
keyList = []
all_ics = np.zeros(shape=(11,), dtype=np.float32)

for n in range(2,11):
    key = utils.get_key(plainText,encryptedText,n)
    if not key is None:
        decryptedText = utils.decryption(encryptedText,key,n)
        all_ics[n] = utils.index_of_coincidence(decryptedText)
        keyList.append(key)
    

keySize = (min(range(len(all_ics)), key=lambda i: abs(all_ics[i]-0.069)))
print('Key Size: ',keySize)
# test = "VVQGYTVVVKALURWFHQACMMVLEHUCATWFHHIPLXHVUWSCIGINCMUHNHQRMSUIMHWZODXTNAEKVVQGYTVVQPHXINWCABASYYMTKSZRCXWRPRFWYHXYGFIPSBWKQAMZYBXJQQABJEMTCHQSNAEKVVQGYTVVPCAQPBSLURQUCVMVPQUTMMLVHWDHNFIKJCPXMYEIOCDTXBJWKQGAN"
# print(utils.index_of_coincidence(encryptedText))
    