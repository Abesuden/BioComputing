import random
import re

nucleotides = ["A", "G", "T", "C"]
purines = ["A", "G"]
pyrimidines = ["T", "C"]
nodes = []
connectors = []
mer = 20

def createNodes(nodeNumber):
	if type(nodeNumber) == int:
		if nodeNumber < 3:
			raise Exception("Insufficient value of " + str(nodeNumber) + " for createNode(), must be > 3.")
	        print("      -==Starting node creation==-")
		print(".--------------------------------------.")
		for i in range(nodeNumber):
			createdNode = _createNode()
			nodes.append(createdNode)
			print("| " + str(i) + " |" + createdNode + " node created |")
		if nodeNumber < 10:
			print("'--------------------------------------'")
		elif nodeNumber > 9 & nodeNumber < 100:
			print("'---------------------------------------'")
		elif nodeNumber > 99:
			print("'----------------------------------------'")
		return nodes
	else:
		raise Exception("Invalid createNodes() argument " + str(type(nodeNumber)) + " must be of <type 'int'>.")

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

def connectNodes(connectNode):
	if not nodes:
		raise Exception("Cannot connect nodes until nodes have been created.")
	if type(connectNode) != list:
		raise Exception("Invalid argument structure " + str(type(connectNode)) + " must be <type 'list'>")
	for ex in range(len(connectNode)):
		if type(connectNode[ex]) != str:
			raise Exception("Invalid connectNodes() argument " + str(type(connectNode[ex])) + " all arguments must be of <type 'str'>")
	print("Initializing node connetctions...")
	regEx = []
	for i in range((len(connectNode))):
		regEx.append(re.findall("^[0-9\s]+|->|[0-9,\s]+|.", connectNode[i]))
	if int(regEx[len(regEx)-1][0]) > (len(nodes)):
		raise Exception("Connot connect " + str(regEx[len(regEx)-1][0]) + " nodes when there are only " + str(len(nodes)) + " nodes that have been created.")
	for elem in regEx:
		temp = elem[2].split(",")
		del elem[1:]
		for j in range(len(temp)):
			elem.append(temp[j])
		if elem[len(elem)-1] == "":
			del elem[len(elem)-1]
	for connect in regEx:
		for elem in range(len(connect)):
			if elem == 0:
				continue
			else:
				if connect[elem].isdigit() == False:
					raise Exception("Invalid argument for node " + connect[0] + "to connect with, must be a number as <type 'str'>.")
				connectors.append(_complimentary(nodes[int(connect[0])][mer/2:]) + _complimentary(nodes[int(connect[elem])][:mer/2]))
	print("")
	print("-==Nodes Connected==-")
	print(".--------------------.")
	for i in connectors:
		print("|" + i + "|")
	print("'--------------------'")
	return connectors

def report():
	if not nodes:
		raise Exception("Cannot make a report until nodes have been created and connected.")
	if not connectors:
		raise Exception("Cannot make a report until nodes have been connected.")
	out = []
	print("Creating Report...")
	fl = open("Hamiltonian_Path_Problem_Report.txt", "w")
	out.append("Report")
	out.append("---------")
	out.append("\n")
	out.append("\n")
	out.append("Nodes:")
	for i in nodes:
		out.append("\n")
		out.append(i)
	out.append("\n")
	out.append("\n")
	out.append("Connectors:")
	for i in connectors:
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
