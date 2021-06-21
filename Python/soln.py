def encode(string):
    encoded_string = ""
    for i in range(0, len(string)-1, 2):
        encoded_string += string[i+1].swapcase() + string[i].swapcase()
    if len(string) % 2 != 0:
        encoded_string += string[-1].swapcase()
    return encoded_string


Encoded = encode('HiMeSh ReShAmIyA Is Bai SeXUAL')
print(Encoded)
print(encode(Encoded))
