import hampath
import sattv

"""
BioComp.changeMer(30)
BioComp.createNodes(7)
BioComp.connectNodes(["0->1,3,6", "1->2,3", "2->1,3", "3->2,4,", "4->1,5", "5->2,6"]) # from research paper
BioComp.report()
"""

"""
SATTruthValue.changeMer(30)
"""
# SATTruthValue.createNodes(["`x1,x2,`x3", "x1,x2,~x3", "`x1,x2,x3"])
# SATTruthValue.createNodes(["`x1,x2,`x3,x4", "x1,x2,~x3,x4", "`x1,x2,x3,x4"])
SATTruthValue.createNodes(["~X3,~X16,~X18", "X5,X12,~X9", "~X13,~X2,X20", "X12,~X9,~X5", "X19,~X4,X6", "X9,X12,~X5", "~X1,X4,X11", "X13,~X2,~X19", "X5,X17,X9", "~X5,~X9,~X12", "X6,X11,X4", "~X15,~X17,X7", "~X6,X19,X13", "~X12,~X9,X5", "X12,X1,X14", "X20,X3,X2", "X10,~X7,~X8", "~X5,X9,~X12", "X18,~X20,X3", "~X10,~X18,~X16", "X1,~X11,~X14", "X8,~X7,~X15", "~X8,X16,~X10"]) # from research paper
SATTruthValue.report()
