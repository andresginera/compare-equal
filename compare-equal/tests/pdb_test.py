import chimera
from algorithms.compare_equal import ComparePdb

out1 = ComparePdb("compare-equal/tests/mol1", "compare-equal/tests/mol2")
out2 = ComparePdb("compare-equal/tests/mol1", "compare-equal/tests/mol3")
out3 = ComparePdb("compare-equal/tests/mol2", "compare-equal/tests/mol3")

if out1 != True:
    print("Error in first comparison: mol1 and mol2")
if out2 != False:
    print("Error in second comparison: mol1 and mol3")
if out3 != False:
    print("Error in third comparison: mol2 and mol3")
