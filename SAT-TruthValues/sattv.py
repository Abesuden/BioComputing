import random
import re

nucleotides = ["A", "G", "T", "C"]
purines = ["A", "G"]
pyrimidines = ["T", "C"]
nodes = []
fishingRods = []
mer = 20
sumNodes = 0

def createNodes(truthValues):
    if type(truthValues) != list:
        raise Exception("Invalid argument structure " + str(type(truthValues)) + " must be <type 'list'>")
    for ex in range(len(truthValues)):
        if type(truthValues[ex]) != str:
            raise Exception("Invalid truthValues() argument " + str(type(truthValues[ex])) + " all arguments must be of <type 'str'>")
    regEx = []
    truthValueCount = []
    argument = []
    for i in range(len(truthValues)):
        regEx.append(re.split(",", truthValues[i]))
    for ex in range(len(regEx)):
        for ez in range(len(regEx[ex])):
            argument.append(re.split("x|X", regEx[ex][ez]))
    for ex in range(len(argument)):
        # print(ord(argument[ex]))
        if (len(argument[ex]) == 1 ):
                raise Exception("Invalid, truthValues() argument is empty at argument position " + str(ex+1))
        for ez in argument[ex]:
            if ((ez != "`") & (ez != "~") & (not ez.isdigit()) & (ez != "")):
                raise Exception("Invalid truthValues() argument format " + str(argument[ex][0]) + "X" + str(argument[ex][1]) + " where [" + str(ez) + "] is not acceptable")
        if ((argument[ex][0] != "") & (argument[ex][0] != "`") & (argument[ex][0] != "~")):
            raise Exception("Invalid truthValues() argument negation " + "(" + str(regEx[ex][0]) + ")" + "X" + str(regEx[ex][1]) + ", the only accepted negation characters are '~' and '`'")
        if (not argument[ex][len(argument[ex])-1].isdigit()):
            raise Exception("Invalid truthValues() argument format at truth value position " + str(ex+1) + " where argument is missing a number assignment [" + str(argument[ex][0]) + "X]")
        # print(argument[ex])
            # if ((len(regEx[ex][ez]) != 2) & (len(regEx[ex][ez]) != 3)):
            #     raise Exception("Invalid truthValues() argument length of " + str(len(regEx[ex][ez])) + " characters, each argument's length must be of size 2 or 3 characters (i.e. x1 or ~x1)")
            # if ((len(regEx[ex][ez]) == 3) & (regEx[ex][ez][0] != '`') & (regEx[ex][ez][0] != '~')):
            #     raise Exception("Invalid truthValues() argument negation " + "(" + str(regEx[ex][ez][0]) + ")" + str(regEx[ex][ez][1]) + str(regEx[ex][ez][2]) + ", the only accepted negation characters are '~' and '`'")
            # if regEx[ex][ez][len(regEx[ex][ez])-1] not in truthValueCount:
            #     truthValueCount.append(regEx[ex][ez][len(regEx[ex][ez])-1])
        if argument[ex][len(argument[ex])-1] not in truthValueCount:
            truthValueCount.append(argument[ex][len(argument[ex])-1])
    nodeNumber = len(regEx) * len(regEx[0])
    print("  -==Starting DNA sequence creation==-")
    print(".---------------------------------------.")
    largestNum = 0
    for elem in range(len(argument)):
        if (int(argument[elem][len(argument[elem])-1]) > largestNum):
            largestNum = int(argument[elem][len(argument[elem])-1])
    excep = 0
    for elem in truthValueCount:
        excep += int(elem)
    for each in truthValueCount:
        excep -= int(each)
    if (excep != 0):
        raise Exception("Invalid truthValues() argument format, truth value assignments cannot skip numbers (i.e. \"x1,x2,x4\" is not an accepted format)")
    for i in range(largestNum*2):
        createdNode = _createNode()
        nodes.append(createdNode)
        if (i < largestNum):
            print("| x" + str(i+1) + " |" + createdNode + " node created |")
        else:
            print("|~x" + str((i-largestNum)+1) + " |" + createdNode + " node created |")
    print("|---------------------------------------'-.")
    for i in range(largestNum+1):
        createdNode = _createNode()
        nodes.append(createdNode)
        if (i == 0):
            print("| Vin|" + createdNode + " vertex created |")
        elif (i == largestNum):
            print("|Vout|" + createdNode + " vertex created |")
        else:
            print("| V" + str(i) + " |" + createdNode + " vertex created |")
    print("|-----------------------------------------'--.")
    global sumNodes
    sumNodes = largestNum
    nodeLocation = 0
    vertexLocation = largestNum*2
    for i in range(largestNum*4):
        if ((i % 4) == 0):
            fishingRods.append(
                _complimentary(nodes[vertexLocation][int(mer/2):]) +
                _complimentary(nodes[nodeLocation][:int(mer/2)])
            )
            print("| C" + str(nodeLocation + 1) + "a|" + fishingRods[i] + " connector created |")
        if ((i % 4) == 1):
            fishingRods.append(
                _complimentary(nodes[nodeLocation][int(mer/2):]) +
                _complimentary(nodes[vertexLocation+1][:int(mer/2)])
            )
            print("| C" + str(nodeLocation + 1) + "b|" + fishingRods[i] + " connector created |")
        if ((i % 4) == 2):
            fishingRods.append(
                _complimentary(nodes[vertexLocation][int(mer/2):]) +
                _complimentary(nodes[nodeLocation+largestNum][:int(mer/2)])
            )
            print("|~C" + str(nodeLocation + 1) + "a|" + fishingRods[i] + " connector created |")
        if ((i % 4) == 3):
            fishingRods.append(
                _complimentary(nodes[nodeLocation+largestNum][int(mer/2):]) +
                _complimentary(nodes[vertexLocation+1][:int(mer/2)])
            )
            print("|~C" + str(nodeLocation + 1) + "b|" + fishingRods[i] + " connector created |")
            nodeLocation += 1
            vertexLocation += 1
    if nodeNumber < 10*2:
        print("'--------------------------------------------'")
    elif nodeNumber > 9*2 & nodeNumber < 100*2:
        print("'---------------------------------------------'")
    elif nodeNumber > 99*2:
        print("'----------------------------------------------'")
    return nodes


def changeMer(newLength):
	if type(newLength) != int:
		raise Exception("Invalid argument for changeMer() of " + str(type(newLength))  + " must be of <type 'int'>")
	if newLength < 20:
		raise Exception("Insufficient value of " + str(newLength) + " for changeMer(), cannot be < 20 mers.")
	if (newLength % 2) == 0:
		global mer
		mer = newLength
	else:
		raise Exception("Invalid argument in changeMer(), new mer must be divisible by two.")
	print("DNA node length has been changed to " + str(mer) + " mers!")

def report():
    if not nodes:
        raise Exception("Cannot make a report until nodes have been created.")
    if not fishingRods:
        raise Exception("Cannot make a report until nodes have had their connections made.")
    out = []
    print("Creating Report...")
    fl = open("SAT_TruthValue_Report.txt", "w")
    out.append("Report")
    out.append("---------")
    out.append("\n")
    out.append("\n")
    for i in range(len(nodes)):
        if (i < (len(nodes)-sumNodes)):
            if (i == 0):
                out.append("Nodes:")
            out.append("\n")
            out.append(nodes[i])
        else:
            if (i == (len(nodes)-sumNodes)):
                out.append("\n")
                out.append("\n")
                out.append("Vertices:")
            out.append("\n")
            out.append(nodes[i])
    out.append("\n")
    out.append("\n")
    out.append("Connectors:")
    for i in fishingRods:
        out.append("\n")
        out.append(i)
    out.append("\n")
    out.append("\n")
    out.append("---END---")
    out.append("\n")
    for i in out:
        fl.write(i)
    fl.close()
    print("")
    print("Report Generated!")

def _createNode():
	twentyMer = ""
	for i in range(mer):
		twentyMer += random.choice(nucleotides)
	return twentyMer

def _complimentary(DNAseq):
	cDNA = []
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