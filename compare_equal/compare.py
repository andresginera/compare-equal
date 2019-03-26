# -*- coding: utf-8 -*-

"""
Main module Compare composed of the two functions for comparison of two molecules.
"""

import os

import chimera
from chimera import match


def compare_pdb(pdb_1, pdb_2):
    """
    Recieves the name (or path) of two PDB files and checks if the two molecules of both 
    PDB files are equals, in which case, it will return a True value.

    Parameters
    ----------
    pdb_1, pdb_2 : str
        The paths from the current working directory to the PDB files to compare.

    Returns
    -------
    bool
        A True or False value depending if both PDB are equal or not.

    """

    path = os.getcwd()
    if not pdb_1.endswith(".pdb"):
        pdb_1 += ".pdb"
    if not pdb_2.endswith(".pdb"):
        pdb_2 += ".pdb"
    mol_1 = chimera.openModels.open(os.path.join(path, pdb_1), type="PDB")[0]
    mol_2 = chimera.openModels.open(os.path.join(path, pdb_2), type="PDB")[0]
    atoms_1 = mol_1.atoms
    atoms_2 = mol_2.atoms
    if mol_1.numAtoms == mol_2.numAtoms:
        rmsd = round(match.matchAtoms(atoms_1, atoms_2)[1], 3)
        return not bool(rmsd)
    return False


def compare_mol(mol_1, mol_2):
    """
    Recieves two 'chimera.Molecule' objects and checks if both are equals, in which case,
    it will return a True value.

    Parameters
    ----------
    mol_1, mol_2 : chimera.Molecule object
        The Python variables to compare with each other.

    Returns
    -------
    bool
        A True or False value depending if both molecules are equal or not. 

    Raises
    ------
    AssertionError
        If one of the arguments **is not** a Chimera Molecule object.

    """

    assert isinstance(
        mol_1, chimera.Molecule
    ), "First variable is not a 'chimera.Molecule' object"
    assert isinstance(
        mol_2, chimera.Molecule
    ), "Second variable is not a 'chimera.Molecule' object"
    atoms_1 = mol_1.atoms
    atoms_2 = mol_2.atoms
    if mol_1.numAtoms == mol_2.numAtoms:
        rmsd = round(match.matchAtoms(atoms_1, atoms_2)[1], 3)
        return not bool(rmsd)
    return False
