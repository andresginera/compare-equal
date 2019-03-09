import sys

sys.path.insert(0, "/home/andres/practicas/root/")

from compare_equal import compare

# As the current directory is the root of the package compare_equal, the directory of the pdb files must be from this directory:

out1 = compare.ComparePdb("tests/mol1", "tests/mol2")
out2 = compare.ComparePdb("tests/mol1", "tests/mol3")
out3 = compare.ComparePdb("tests/mol2", "tests/mol3")

if out1 != True:
    print("Error in first comparison: mol1 and mol2")
if out2 != False:
    print("Error in second comparison: mol1 and mol3")
if out3 != False:
    print("Error in third comparison: mol2 and mol3")
