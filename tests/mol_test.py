# -*- coding: utf-8 -*-

"""
Test for the function compare_equal.compare.CompareMol

Returns no output if the package was correctly installed.
"""

import os
import sys

sys.path.append("../..")
path = os.path.dirname(os.path.abspath(__file__))

import chimera
from compare_equal import compare

# Definition of 3 variable of Molecule class wih local PDF files

mol1 = chimera.openModels.open(path + "/data/mol1.pdb", type="PDB")[0]
mol2 = chimera.openModels.open(path + "/data/mol2.pdb", type="PDB")[0]
mol3 = chimera.openModels.open(path + "/data/mol3.pdb", type="PDB")[0]

out1 = compare.compare_mol(mol1, mol2)
out2 = compare.compare_mol(mol1, mol3)
out3 = compare.compare_mol(mol2, mol3)

assert out1 == True, "Error in first comparison: mol1 and mol2"
assert out2 == False, "Error in second comparison: mol1 and mol3"
assert out3 == False, "Error in third comparison: mol2 and mol3"
