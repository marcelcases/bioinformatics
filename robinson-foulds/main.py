"""
Robinson-Foulds distance between two phylogenetic trees
MIRI-BSG
Marcel Cases Freixenet
Autumn 2021

It is defined as (A + B) where A is the number of partitions of data implied by
the first tree but not the second tree and B is the number of partitions of data
implied by the second tree but not the first tree.

The partitions are calculated for each tree by removing each branch.

The number of eligible partitions for each tree is equal to the number of branches in that tree.
"""

from Bio import Phylo
from io import StringIO
import os

FOLDER_TOP = os.path.dirname(os.path.abspath(__file__))

class  RobinsonFoulds():
    def __init__(self):
        super().__init__()

class Draw():
    def __init__(self):
        super().__init__()
    
    def raw(self, tree):
        print(tree)
    
    def ascii(self, tree):
        Phylo.draw_ascii(tree)
    
    def plot(self, tree):
        tree.ladderize()  # Flip branches so deeper clades are displayed at top
        Phylo.draw(tree)
    
    def dendrogram(self, tree):
        Phylo.draw_graphviz(tree)

if __name__ == "__main__":
    draw = Draw()
    rf = RobinsonFoulds()
    tree1a = Phylo.read(FOLDER_TOP+'/example.xml','phyloxml')
    tree1b = Phylo.read(StringIO("((A, B), C)"), "newick")
    tree2 = Phylo.read(StringIO("(A, (B, C), (D, E))"), "newick")
    # draw.raw(tree1)
    # draw.ascii(tree1a)
    # draw.ascii(tree1b)
    draw.plot(tree1b)
    # draw.dendrogram(tree1b)
