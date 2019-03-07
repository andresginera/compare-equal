# I found this solution for a problem regarding the importing of local Python module from others directories.

import sys
from os.path import dirname, abspath, join, sep

compare_equal = dirname(dirname(abspath(__file__)))
assert compare_equal.split(sep)[-1].lower() == "compare-equal"
sys.path.append(compare_equal)

# Both tests have to be run in the main root: COMPARE_EQUAL and with pychimera:
# $ ~/practicas/compare_equal$ pychimera -m compare-equal.tests.pdb_test

