# -*- coding: utf-8 -*-

"""
Main module Compare composed of the two functions for comparison of two molecules.
"""

import os

import chimera
import chimera.match as match


def ComparePdb(pdb_1, pdb_2):
    """
    Recieves the name (or path) of two PDB files and checks if the two molecules of both 
    PDB files are equals, in which case, it will return a True value.


    Parameters:
        - pdb_1 (str): The path from the current working directory to the first PDB file 
                       to compare.
        - pdb_2 (str): The path from the current working directory to the second PDB file
                       to compare.
    
    Returns:
        A True or False value depending if both PDB are equal or not (Boolean).
    """
    path = os.getcwd()
    if not pdb_1.endswith(".pdb"):
        pdb_1 += ".pdb"
    if not pdb_2.endswith(".pdb"):
        pdb_2 += ".pdb"
    mol_1 = chimera.openModels.open("{0}/{1}".format(path, pdb_1), type="PDB")[0]
    mol_2 = chimera.openModels.open("{0}/{1}".format(path, pdb_2), type="PDB")[0]
    atoms_1 = mol_1.atoms
    atoms_2 = mol_2.atoms
    if mol_1.numAtoms == mol_2.numAtoms:
        rmsd = float("{0:.3f}".format(match.matchAtoms(atoms_1, atoms_2)[1]))
        if rmsd == 0:
            return True
        else:
            return False
    else:
        return False


def CompareMol(mol_1, mol_2):
    """
    Recieves two 'chimera.Molecule' objects and checks if both are equals, in which case,
    it will return a True value.


    Parameters:
        - mol_1 ('chimera.Molecule' object): A Python variable to compare with *mol_2*.
        - mol_2 ('chimera.Molecule' object): A Python variable to compare with *mol_1*.
    
    Returns:
        A True or False value depending if both molecules are equal or not (Boolean). 
    
    Raises:
        - AssertionError if one of the arguments is not a Chimera Molecule object.
    """
    assert (
        type(mol_1) == chimera.Molecule
    ), "First variable is not a 'chimera.Molecule' object"
    assert (
        type(mol_2) == chimera.Molecule
    ), "Second variable is not a 'chimera.Molecule' object"
    atoms_1 = mol_1.atoms
    atoms_2 = mol_2.atoms
    if mol_1.numAtoms == mol_2.numAtoms:
        rmsd = float("{0:.3f}".format(match.matchAtoms(atoms_1, atoms_2)[1]))
        if rmsd == 0:
            return True
        else:
            return False
    else:
        return False
