"""
Compare-Equal is a package composed of two modules for for comparison two molecules and checks if they are the same molecule.

The main module is :mod:`compare_equal.compare` which contains the two main function: the :function:`compare_equal.compare.ComparePdb`, 
for comparing the molecules inside of two PDB files, and the :function:`compare_equal.compare.CompareMol, for comparing two 'chimera.Molecule' 
objects. These two function can be imported directly with the package compare_equal or, also, importing the module :mod:`compare_equal.compare`.

Moreover, the package includes another module for check the properly running of the two function, the :mod:`compare_equal.tests`. 
"""

__author__ = "Andrés Giner Antón"
__url__ = "https://github.com/andresginera/compare-equal"
__title__ = "Compare Equal"
__description__ = (
    "A test package for practising Git software and Python package development."
)
__all__ = ["ComparePdb", "CompareMol"]
from compare import *
