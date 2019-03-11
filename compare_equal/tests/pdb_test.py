import sys
import os

sys.path.append("../..")

from compare_equal import compare

path = os.path.dirname(os.path.abspath(__file__))

out1 = compare.ComparePdb(path + "data/mol1", path + "data/mol2")
out2 = compare.ComparePdb(path + "data/mol1", path + "data/mol3")
out3 = compare.ComparePdb(path + "data/mol2", path + "data/mol3")

if out1 != True:
    print("Error in first comparison: mol1 and mol2")
if out2 != False:
    print("Error in second comparison: mol1 and mol3")
if out3 != False:
    print("Error in third comparison: mol2 and mol3")
