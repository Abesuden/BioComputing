import random
import re

nucleotides = ["A", "G", "T", "C"]
purines = ["A", "G"]
pyrimidines = ["T", "C"]
nodes = []
fishingRods = []
mer = 20

def createNodes(truthValues):
    if type(truthValues) != list:
        raise Exception("Invalid argument structure " + str(type(truthValues)) + " must be <type 'list'>")
    for ex in range(len(truthValues)):
        if type(truthValues[ex]) != str:
            raise Exception("Invalid truthValues() argument " + str(type(truthValues[ex])) + " all arguments must be of <type 'str'>")
    regEx = []
    for i in range(len(truthValues)):
        regEx.append(re.split(",", truthValues[i]))
    nodeNumber = len(regEx) * len(regEx[0])
    print("      -==Starting node creation==-")
    print(".---------------------------------------.")
    largestNum = 0
    for elem in range(len(regEx)):
        for subElem in range(len(regEx[elem])):
            if (regEx[elem][subElem][len(regEx[elem][subElem])-1] > largestNum):
                largestNum = int(regEx[elem][subElem][len(regEx[elem][subElem])-1])
    for i in range(largestNum*2):
        createdNode = _createNode()
        nodes.append(createdNode)
        if (i < largestNum):
            print("| x" + str(i+1) + " |" + createdNode + " node created |")
        else:
            print("|~x" + str((i-largestNum)+1) + " |" + createdNode + " node created |")
    print("|---------------------------------------|")
    for i in range(largestNum+1):
        createdNode = _createNode()
        nodes.append(createdNode)
        if (i == 0):
            print("| Vin|" + createdNode + " node created |")
        elif (i == largestNum):
            print("|Vout|" + createdNode + " node created |")
        else:
            print("| V" + str(i) + " |" + createdNode + " node created |")
    print("|---------------------------------------'----.")
    nodeLocation = 0
    vertexLocation = largestNum*2
    for i in range(largestNum*4):
        if ((i % 4) == 0):
            fishingRods.append(
                _complimentary(nodes[vertexLocation][mer/2:]) +
                _complimentary(nodes[nodeLocation][:mer/2])
            )
            print("| C" + str(nodeLocation + 1) + "a|" + fishingRods[i] + " connector created |")
        if ((i % 4) == 1):
            fishingRods.append(
                _complimentary(nodes[nodeLocation][mer/2:]) +
                _complimentary(nodes[vertexLocation+1][:mer/2])
            )
            print("| C" + str(nodeLocation + 1) + "b|" + fishingRods[i] + " connector created |")
        if ((i % 4) == 2):
            fishingRods.append(
                _complimentary(nodes[vertexLocation][mer/2:]) +
                _complimentary(nodes[nodeLocation+largestNum][:mer/2])
            )
            print("|~C" + str(nodeLocation + 1) + "a|" + fishingRods[i] + " connector created |")
        if ((i % 4) == 3):
            fishingRods.append(
                _complimentary(nodes[nodeLocation+largestNum][mer/2:]) +
                _complimentary(nodes[vertexLocation+1][:mer/2])
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