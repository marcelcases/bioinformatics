"""
# Lab 1: Robinson-Foulds distance

Implementation in Python of the quadratic-time algorithm for the Robinson-Foulds distance between two phylogenetic trees.

## About

**Course**  
Bioinformatics and Statistical Genetics (BSG-MIRI)  
FIB - Universitat Politècnica de Catalunya. BarcelonaTech  
Autumn 2021  

**Team**  
* Antoni Casas
&lt;antoni.casas.munoz@estudiantat.upc.edu&gt;
* Marcel Cases
&lt;marcel.cases@estudiantat.upc.edu&gt;
"""

"""
## The algorithm

We use `ete3` as the library for parsing phylogenetic trees from a string.
We use the Newick representation.
"""

from ete3 import Tree

# Loads a tree structure from a newick string. The returned variable ’t’ is the root node for the tree.
t = Tree("(((1,2),3),4);" )
t2 = Tree("(1,(2,(3,4)));" )


"""
The input trees that we want to use for calculating the distance with the Robinson-Foulds algorithm are the following two:
"""

print("t:", t)
print("t2:", t2)


"""
We build a recursive function that takes each child from the node up to the last in each branch and applies a reverse process in order to identify sets from nodes
"""

def reverseTraversal(node, resultSet):
    currentClust=set()
    for child in node.children:
        leafClust=reverseTraversal(child,resultSet)
        currentClust=currentClust.union(leafClust)
    currentClust=currentClust.union(node.name)
    resultSet.append(currentClust)
    return currentClust


"""
Once we have identified all sets in each tree, ...
"""

sets1=[]
reverseTraversal(t,sets1)
print("Sets 1:", sets1)

sets2=[]
reverseTraversal(t2,sets2)
print("Sets 2:", sets2)


lenSets1=len(sets1)
lenSets2=len(sets2)

distance=0

for val in sets1:
    contained=False
    currentIt=0
    while not contained and currentIt<len(sets2):
        auxVal=sets2[currentIt]
        if (auxVal==val):
            contained=True
        currentIt=currentIt+1
    if (not contained):
        distance=distance+1

for val in sets2:
    contained=False
    currentIt=0
    while not contained and currentIt<len(sets1):
        auxVal=sets1[currentIt]
        if (auxVal==val):
            contained=True
        currentIt=currentIt+1
    if (not contained):
        distance=distance+1


"""
Finally, the computed distance between ``t`` and ``t2`` is:
"""

print("R-F distance:", distance)
