import utils

plainText = "SHORTEXAMPLE"
encryptedText = "APADJTFTWLFJ"

assert len(plainText)==len(encryptedText)

# for n in range(1,11):
#     known_plainText = plainText[:n*n]
#     known_encryptedText = encryptedText[:n*n]
#     currentKey = utils.getKey(known_plainText,known_encryptedText,n)
#     print(known_encryptedText)

key = utils.get_key(plainText,encryptedText,2)
print(key)


# test = "VVQGYTVVVKALURWFHQACMMVLEHUCATWFHHIPLXHVUWSCIGINCMUHNHQRMSUIMHWZODXTNAEKVVQGYTVVQPHXINWCABASYYMTKSZRCXWRPRFWYHXYGFIPSBWKQAMZYBXJQQABJEMTCHQSNAEKVVQGYTVVPCAQPBSLURQUCVMVPQUTMMLVHWDHNFIKJCPXMYEIOCDTXBJWKQGAN"
# print(utils.index_of_coincidence(encryptedText))
    