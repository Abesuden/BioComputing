
# the binary representation of "1111" is as follows: binaryEight binaryFour binaryTwo binaryOne
binaryEight = ["G", "A", "G", "A", "G"]
binaryFour = ["T", "T", "T", "T", "T"]
binaryTwo = ["A", "A", "A", "A", "A"]
binaryOne = ["C", "C", "C", "C", "C"]
substrandLen = 5

# init global variables
memoryComplex = []
isMemCompCreated = False

def memoryComplexLen(MCL): # by nucleotide number

    # pull in global variables
    global isMemCompCreated
    
    # raise exceptions
    if (isMemCompCreated):
        print("Error: only one memory complex can be created, which means only one creation method can be used... [i.e. biteSize() or byteSize()]")
    if (type(MCL) != int):
        print("not int")
    # if (not MCL.isdigit):
    #     print("not numeric")
    if ((MCL%5) != 0):
        print("needs to be in increments of 5")
    if (MCL < 1):
        print("needs to be a positive number")

    # find length of requested DNA strand in units of DNA's binary representation
    counter = MCL/substrandLen

    # create memory complex by repeating 1111 1111 1111 1111...
    for i in range(counter):
        if ((i % 4) == 0):
            memoryComplex.append(binaryEight)
        if ((i % 4) == 1):
            memoryComplex.append(binaryFour)
        if ((i % 4) == 2):
            memoryComplex.append(binaryTwo)
        if ((i % 4) == 3):
            memoryComplex.append(binaryOne)
    isMemCompCreated = True

def bitSize(bits): # by increments of 5 nucleotides
    
    # pull in global variables
    global isMemCompCreated

    # raise exceptions
    if (isMemCompCreated):
        print("Error: only one memory complex can be created, which means only one creation method can be used... [i.e. memoryComplexLen() or byteSize()]")
    if (type(bits) != int):
        print("needs to be of type int")
    if (bits < 1):
        print("needs to be a positive number")
    isMemCompCreated = True

def byteSize(byte): # by increments of 8 bits (aka. 40 nucleotides)

    # pull in global variables
    global isMemCompCreated

    # raise exceptions
    if (isMemCompCreated):
        print("Error: only one memory complex can be created, which means only one creation method can be used... [i.e. memoryComplexLen() or biteSize()]")
    if (type(byte) != int):
        print("needs to be of type int")
    if (byte < 1):
        print("needs to be a positive number")
    isMemCompCreated = True

def report():
    if (not isMemCompCreated):
        print("Error: report() can only be used once a memory complex has been can be created [i.e. memoryComplexLen(), biteSize() or byteSize()]")
    
