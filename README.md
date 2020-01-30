# BioComputing
Python modules for biologists wanting to easily generate DNA sequences used to solve NP-complete problems in polynomial time in a wet lab. Feel free to fork and use in exchange for a reference/acknowledgement in the research article (if applicable). Contact me if you are interested in collaborating.

#### Python module names
* **[hampath](https://github.com/Abesuden/BioComputing/blob/master/README.md#hampath-hamiltonian-path-problem)**
* **[sattv](https://github.com/Abesuden/BioComputing/blob/master/README.md#sattv-sat-truth-value-problem)**

#### Python module TBA
```
satg
kcol
```

## hampath (Hamiltonian Path Problem)
  Can be found in the hamiltonianPath folder and is used to generate nodes and connections from nucleotides. The output from this program will give the exact DNA sequences you need to order to work on this problem.

#### Examples of methods
```
changeMer(30)   <-- changes the DNA length of each node/connector
createNodes(7)  <-- creates 7 nodes in this example
connectNodes(["0->1,3,6", "1->2,3", "2->1,3", "3->2,4,", "4->1,5", "5->2,6"])  <-- tells which node points where (ie. 0 points to 1,3,6)
report()        <-- generates a text file with the DNA sequences for the nodes and connectors
```

## sattv (SAT Truth Value Problem)
  Can be found in the hamiltonianPath folder and is used to generate nodes and connections from nucleotides. The output from this program will give the exact DNA sequences you need to order to work on this problem.

#### Examples of methods
```
changeMer(30)   <-- changes the DNA length of each node/connector
createNodes(["`X1,`X2,X2", "X1,`X2,`X3", "`X1,X2,X3"])  <-- creates all truth value nodes, Vin, Vout, and connector nodes
report()        <-- generates a text file with the DNA sequences for all truth value nodes, Vin, Vout, and connector nodes
```

#### Alternative truth value negation arguments
```
createNodes(["~X1,~X2,X2", "X1,~X2,~X3", "~X1,X2,X3"])
```
