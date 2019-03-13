User Guide
========================

Compare Equal is a package of two function and a subpackage of tests for each function. As the package uses Chimera classes and its attributes, it is essential to have it installed. The package imports the Chimera module:

.. literalinclude:: ../compare_equal/compare.py
    :language: python
    :lines: 3-4

------------
Functions
------------

The functions are ComparePdb for comparing two PDB files and CompareMol for comparing two Python variable of the Chimera class Molecule.
Both function return a boolean value (True or False) depending if both molecules are equal not.


.. py:function:: ComparePdb(pdb_1,pdb_2)

    Recieves the name of two PDB files with or without extension and checks 
    if the two molecules of both PDB files are equals, in which case, 
    it will return a ``True`` value.

    :param str pdb_1: The path from the current working directory to the first PDB file to compare.
    :param str pdb_2: The path from the current working directory to the second PDB file to compare.
    :return: A True or False value.
    :rtype: Boolean.

.. py:function:: CompareMol(mol_1,mol_2)

    Recieves two ``'chimera.Molecule' objects`` and checks
    if both are equals, in which case, it will return a ``True`` value.

    :param mol_1: A Python variable to compare with *mol_2*.
    :param mol_2: A Python variable to compare with *mol_1*.
    :type mol_1: 'chimera.Molecule' object
    :type mol_2: 'chimera.Molecule' object
    :return: A True or False value.
    :rtype: Boolean.
    :raises AssertionError: if one of the arguments is not a Chimera Molecule object.