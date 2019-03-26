# -*- coding: utf-8 -*-

"""
Compare Equal is a package composed of two functions for comparison two molecules and checks 
if they are the same molecule. The package uses Chimera classes and its attributes, so, t is 
essential to have it installed. See how to install it in the section: :ref:`install_chimera`.

The main module is :mod:`compare_equal.compare` which contains the two main functions: 
:func:`compare_equal.compare.compare_pdb`, for comparing the molecules inside of two PDB files,
and :func:`compare_equal.compare.compare_mol`, for comparing two 'chimera.Molecule' objects. 
These two functions can be imported directly with the package or, also, importing 
the module :mod:`compare_equal.compare`.

"""

__author__ = "Andres Giner Anton"
__url__ = "https://github.com/andresginera/compare-equal"
__title__ = "Compare Equal"

__all__ = ["compare_pdb", "compare_mol"]
from compare import *
