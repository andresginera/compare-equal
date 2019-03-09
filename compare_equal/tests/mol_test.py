import sys

sys.path.insert(0, "/home/andres/practicas/root/compare_equal")

import chimera
from compare_equal import compare

# Definition of 3 variable of Molecule class wih local PDF files

mol1 = chimera.openModels.open(
    "/home/andres/practicas/root/compare_equal/tests/mol1.pdb", type="PDB"
)[0]
mol2 = chimera.openModels.open(
    "/home/andres/practicas/root/compare_equal/tests/mol2.pdb", type="PDB"
)[0]
mol3 = chimera.openModels.open(
    "/home/andres/practicas/root/compare_equal/tests/mol3.pdb", type="PDB"
)[0]

out1 = compare.CompareMol(mol1, mol2)
out2 = compare.CompareMol(mol1, mol3)
out3 = compare.CompareMol(mol2, mol3)

if out1 != True:
    print("Error in first comparison: mol1 and mol2")
if out2 != False:
    print("Error in second comparison: mol1 and mol3")
if out3 != False:
    print("Error in third comparison: mol2 and mol3")
