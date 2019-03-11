import os

import chimera
import chimera.match as match

path = os.getcwd()


def ComparePdb(pdb_1, pdb_2):
    """
    Recieves the name of two pdb files with or without extension and checks 
    if the two molecules of both pdb files are equals, in which case, 
    it will return a True value.
    """
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
    Recieves two 'chimera.Molecule' objects and checks
    if both are equals, in which case, it will return a True value.
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
