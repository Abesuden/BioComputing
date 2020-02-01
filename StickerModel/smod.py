# the binary representation of "1111" is as follows: binaryEight binaryFour binaryTwo binaryOne
binaryEight = ["G", "A", "G", "A", "G"]
binaryFour = ["T", "T", "T", "T", "T"]
binaryTwo = ["A", "A", "A", "A", "A"]
binaryOne = ["C", "C", "C", "C", "C"]
substrandLen = 5

# init global variables
memoryComplex = []
# stickers = []
memComPrintBuffer = []
isMemCompCreated = False

def memoryComplexLen(MCL): # by nucleotide number

    # pull in global variables
    global isMemCompCreated
    
    # raise exceptions
    if (isMemCompCreated):
        raise Exception("Error: only one memory complex can be created, which means only one creation method can be used... [i.e. memoryComplexLen(), biteSize() or byteSize()]")
    if (type(MCL) != int):
        raise Exception("Invalid memoryComplexLen() argument of " + str(type(MCL)) + " must be of <type 'int'>")
    if ((MCL%5) != 0):
        raise Exception("Invalid memoryComplexLen() argument size, the number needs to be in increments of 5...")
    if (MCL < 1):
        raise Exception("Invalid memoryComplexLen() argument, needs to be a positive number...")

    # find length of requested DNA strand in units of DNA's binary representation
    counter = MCL/substrandLen

    # create memory complex by repeating 1111 1111 1111 1111...
    for i in range(counter):
        if ((i % 4) == 0):
            memoryComplex.append(binaryEight)
            # stickers.append(_complimentary("".join(binaryEight))) # deprecated
        if ((i % 4) == 1):
            memoryComplex.append(binaryFour)
            # stickers.append(_complimentary("".join(binaryFour))) # deprecated
        if ((i % 4) == 2):
            memoryComplex.append(binaryTwo)
            # stickers.append(_complimentary("".join(binaryTwo))) # deprecated
        if ((i % 4) == 3):
            memoryComplex.append(binaryOne)
            # stickers.append(_complimentary("".join(binaryOne))) # deprecated
    
    # display to users
    _printMC()
    _printStickers()

    # turn on flag so other memory complex functions cannot be called
    isMemCompCreated = True

def bitSize(bits): # by increments of 5 nucleotides
    
    # pull in global variables
    global isMemCompCreated

    # raise exceptions
    if (isMemCompCreated):
        raise Exception("Error: only one memory complex can be created, which means only one creation method can be used... [i.e. memoryComplexLen(), biteSize() or byteSize()]")
    if (type(bits) != int):
        raise Exception("Invalid bitSize() argument of " + str(type(bits)) + " needs to be of <type 'int'>")
    if (bits < 1):
        raise Exception("Invalid bitSize() argument, needs to be a positive number")

    # build memory complex
    for i in range(bits):
        if ((i % 4) == 0):
            memoryComplex.append(binaryEight)
            # stickers.append(_complimentary("".join(binaryEight))) # deprecated
        if ((i % 4) == 1):
            memoryComplex.append(binaryFour)
            # stickers.append(_complimentary("".join(binaryFour))) # deprecated
        if ((i % 4) == 2):
            memoryComplex.append(binaryTwo)
            # stickers.append(_complimentary("".join(binaryTwo))) # deprecated
        if ((i % 4) == 3):
            memoryComplex.append(binaryOne)
            # stickers.append(_complimentary("".join(binaryOne))) # deprecated
    
    # display to users
    _printMC()
    _printStickers()

    # turn on flag so other memory complex functions cannot be called
    isMemCompCreated = True

def byteSize(byte): # by increments of 8 bits (aka. 40 nucleotides)

    # pull in global variables
    global isMemCompCreated

    # raise exceptions
    if (isMemCompCreated):
        raise Exception("Error: only one memory complex can be created, which means only one creation method can be used... [i.e. memoryComplexLen(), biteSize() or byteSize()]")
    if (type(byte) != int):
        raise Exception("Invalid byteSize() argument of " + str(type(byte)) + " needs to be of <type 'int'>")
    if (byte < 1):
        raise Exception("Invalid byteSize() argument, needs to be a positive number")
    
    # build memory complex
    for i in range(byte*5*8):
        if ((i % 4) == 0):
            memoryComplex.append(binaryEight)
            # stickers.append(_complimentary("".join(binaryEight))) # deprecated
        if ((i % 4) == 1):
            memoryComplex.append(binaryFour)
            # stickers.append(_complimentary("".join(binaryFour))) # deprecated
        if ((i % 4) == 2):
            memoryComplex.append(binaryTwo)
            # stickers.append(_complimentary("".join(binaryTwo))) # deprecated
        if ((i % 4) == 3):
            memoryComplex.append(binaryOne)
            # stickers.append(_complimentary("".join(binaryOne))) # deprecated
    
    # display to users
    _printMC()
    _printStickers()

    # turn on flag so other memory complex functions cannot be called
    isMemCompCreated = True

def report():

    # raise exceptions
    if (not isMemCompCreated):
        raise Exception("Error: report() can only be used once a memory complex has been can be created [i.e. memoryComplexLen(), biteSize() or byteSize()]")

    # display update to users
    print("Creating Report...")

    # write memory complex and stickers to a text file
    fl = open("stickerModel_Report.txt", "w")
    fl.write("Memory Complex:")
    fl.write("\n")
    fl.write("---------------")
    fl.write("\n")
    fl.write("".join(memComPrintBuffer))
    fl.write("\n")
    fl.write("\n")
    fl.write("Stickers:")
    fl.write("\n")
    fl.write("---------")
    fl.write("\n")
    fl.write(_complimentary(binaryEight))
    fl.write("\n")
    fl.write(_complimentary(binaryFour))
    fl.write("\n")
    fl.write(_complimentary(binaryTwo))
    fl.write("\n")
    fl.write(_complimentary(binaryOne))
    fl.close()
    print("")
    print("Report Created!")

def _printMC():

    # display to users
    print("-==Memory Complex==-")

    # loop unrolling (used to decrease computation time)
    for i in range(len(memoryComplex)):
        memComPrintBuffer.append(memoryComplex[i][0])
        memComPrintBuffer.append(memoryComplex[i][1])
        memComPrintBuffer.append(memoryComplex[i][2])
        memComPrintBuffer.append(memoryComplex[i][3])
        memComPrintBuffer.append(memoryComplex[i][4])
    
    # print out one continuous DNA strand
    print "".join(memComPrintBuffer)
    print("")

def _printStickers():
    
    # print out one line of stickers
    print(" -==Stickers==-")
    print(".-------------.")
    print("|    " + _complimentary(binaryEight) + "    |")
    print("|    " + _complimentary(binaryFour)  + "    |")
    print("|    " + _complimentary(binaryTwo)   + "    |")
    print("|    " + _complimentary(binaryOne)   + "    |")
    print("'-------------'")
    print("")

    # # display to users (deprecated in exchange for more professional display)
    # counter = 0
    # print("\n")
    # print("-==Stickers==-")
    # print(".------------.")
    # for elem in stickers:
    #     print("|    " + elem + "    |")
    #     counter += 1
    #     if (counter == 10):
    #         print("|    -----    |")
    #         print("'    - - -    '")
    #         print("'    -- --    '")
    #         print(".     - -     .")
    #         print("\n")
    #         break
    #     elif (counter == (len(stickers)-1)):
    #         print("'-------------'")
    #         print("\n")

def _complimentary(DNAseq):
	
    # init variable
    cDNA = []

    # create a complimentary strand of DNA
    for nuc in DNAseq:
        if nuc == "A":
            cDNA.append("T")
        elif nuc == "T":
            cDNA.append("A")
        elif nuc == "G":
            cDNA.append("C")
        elif nuc == "C":
            cDNA.append("G")
    return("".join(cDNA))
