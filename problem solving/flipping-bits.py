
def flippingBits(n):
    # print("length: ", end="")
    # print(len(bin(n)))
    # print("type: ", end="")
    # print(type(bin(n)))
    binary = bin(n)[2:]
    binaryLength = len(binary)
    fullBinary = "0"*(32-binaryLength) + binary
    inverse = ""
    # print("full binary: ", end="")
    # print(fullBinary)

    for i in fullBinary:
        if i == '0':
            inverse += '1'
        else:
            inverse += '0'
    
    # print("inverse binary: ", end="")
    # print(inverse)
    
    return int(inverse, 2)


print(flippingBits(4))
print(flippingBits(123456))