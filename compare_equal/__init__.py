# -*- coding: utf-8 -*-

"""
Compare Equal is a package composed of two functions for for comparison two molecules and checks if they are the same molecule.

The main module is `compare_equal.compare` which contains the two main function: `compare_equal.compare.ComparePdb`, 
for comparing the molecules inside of two PDB files, and `compare_equal.compare.CompareMol, for comparing two 'chimera.Molecule' 
objects. These two function can be imported directly with the package compare_equal or, also, importing the module `compare_equal.compare`.

Moreover, the package includes a subpackage for check the properly running of the two function, the `compare_equal.tests`. 
"""

__author__ = "Andres Giner Anton"
__url__ = "https://github.com/andresginera/compare-equal"
__title__ = "Compare Equal"

__all__ = ["ComparePdb", "CompareMol"]
from compare import *
