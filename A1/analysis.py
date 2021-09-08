import utils

plainText = "ABCDEEEGHX"
encryptedText = "CDINMUQABF"

assert len(plainText)==len(encryptedText)



# for n in range(1,11):
#     known_plainText = plainText[:n*n]
#     known_encryptedText = encryptedText[:n*n]
#     print(known_encryptedText)

test = "VVQGYTVVVKALURWFHQACMMVLEHUCATWFHHIPLXHVUWSCIGINCMUHNHQRMSUIMHWZODXTNAEKVVQGYTVVQPHXINWCABASYYMTKSZRCXWRPRFWYHXYGFIPSBWKQAMZYBXJQQABJEMTCHQSNAEKVVQGYTVVPCAQPBSLURQUCVMVPQUTMMLVHWDHNFIKJCPXMYEIOCDTXBJWKQGAN"
print(utils.index_of_coincidence(encryptedText))
    