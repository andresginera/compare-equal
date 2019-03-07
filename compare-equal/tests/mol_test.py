import chimera
from .algorithms import CompareMol

# Definition of 3 variable of Molecule class wih local PDF files

mol1 = chimera.openModels.open("./mol1.pdb".format(pdb_1), type="PDB")[0]
mol2 = chimera.openModels.open("./mol2.pdb".format(pdb_1), type="PDB")[0]
mol3 = chimera.openModels.open("./mol3.pdb".format(pdb_1), type="PDB")[0]

out1 = CompareMol(mol1, mol2)
out2 = CompareMol(mol1, mol3)
out3 = CompareMol(mol2, mol3)

if out1 != True:
    print("Error in first comparison: mol1 and mol2")
if out2 != False:
    print("Error in second comparison: mol1 and mol3")
if out3 != False:
    print("Error in third comparison: mol2 and mol3")
