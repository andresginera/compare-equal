import sys
import os

sys.path.append("../..")

from compare_equal import compare

# As the current directory is the root of the package compare_equal, the directory of the pdb files must be from this directory:

out1 = compare.ComparePdb("data/mol1", "data/mol2")
out2 = compare.ComparePdb("data/mol1", "data/mol3")
out3 = compare.ComparePdb("data/mol2", "data/mol3")

if out1 != True:
    print("Error in first comparison: mol1 and mol2")
if out2 != False:
    print("Error in second comparison: mol1 and mol3")
if out3 != False:
    print("Error in third comparison: mol2 and mol3")
