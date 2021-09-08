from numpy import dtype, float32
import numpy as np
import utils

plainText = "SHORTEXAMPLE"
encryptedText = "APADJTFTWLFJ"

assert len(plainText)==len(encryptedText)

all_ics = np.zeros(shape=(11,), dtype=np.float32)

for n in range(2,11):
    key = utils.get_key(plainText,encryptedText,n)
    all_ics[n] = utils.index_of_coincidence()
    print(key)


# test = "VVQGYTVVVKALURWFHQACMMVLEHUCATWFHHIPLXHVUWSCIGINCMUHNHQRMSUIMHWZODXTNAEKVVQGYTVVQPHXINWCABASYYMTKSZRCXWRPRFWYHXYGFIPSBWKQAMZYBXJQQABJEMTCHQSNAEKVVQGYTVVPCAQPBSLURQUCVMVPQUTMMLVHWDHNFIKJCPXMYEIOCDTXBJWKQGAN"
# print(utils.index_of_coincidence(encryptedText))
    