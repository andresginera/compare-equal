# -*- coding: utf-8 -*-

"""
Test for the function compare_equal.compare.ComparePdb

Returns no output if the package was correctly installed.
"""

import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("../..")
print os.getcwd()
print 


from compare_equal import compare

out1 = compare.compare_pdb("tests/data/mol1", "tests/data/mol2")
out2 = compare.compare_pdb("tests/data/mol1", "tests/data/mol3")
out3 = compare.compare_pdb("tests/data/mol2", "tests/data/mol3")

assert out1 == True, "Error in first comparison: mol1 and mol2"
assert out2 == False, "Error in second comparison: mol1 and mol3"
assert out3 == False, "Error in third comparison: mol2 and mol3"
