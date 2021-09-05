import numpy as np
import sympy

plainText = "ABCDEEEGHX"
encryptedText = "CDINMUQABF"

assert len(plainText)==len(encryptedText)

def index_of_coincidence(s):
    N = len(s)
    freq = [s.count(chr(i+ord('A'))) for i in range(26)]
    print(freq)
    ic = ((float)(sum([i*(i-1) for i in freq])))/(float)(N*(N-1))
    return ic

# for n in range(1,11):
#     known_plainText = plainText[:n*n]
#     known_encryptedText = encryptedText[:n*n]
#     print(known_encryptedText)

test = "VVQGYTVVVKALURWFHQACMMVLEHUCATWFHHIPLXHVUWSCIGINCMUHNHQRMSUIMHWZODXTNAEKVVQGYTVVQPHXINWCABASYYMTKSZRCXWRPRFWYHXYGFIPSBWKQAMZYBXJQQABJEMTCHQSNAEKVVQGYTVVPCAQPBSLURQUCVMVPQUTMMLVHWDHNFIKJCPXMYEIOCDTXBJWKQGAN"
print(index_of_coincidence(encryptedText))
    