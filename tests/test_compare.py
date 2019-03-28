import sys
import os
from pychimera import patch_environ, enable_chimera

patch_environ()
# enable_chimera()

import chimera
from compare_equal import compare


def test_pdb():
    """Test fot the function compare_pdb"""

    assert compare.compare_pdb("tests/data/mol1", "tests/data/mol2")
    assert not compare.compare_pdb("tests/data/mol1", "tests/data/mol3")
    assert not compare.compare_pdb("tests/data/mol2", "tests/data/mol3")


def test_mol():
    """Test fot the function compare_mol"""

    mol_1 = chimera.openModels.open(os.path.abspath("tests/data/mol1.pdb"), type="PDB")[
        0
    ]
    mol_2 = chimera.openModels.open(os.path.abspath("tests/data/mol2.pdb"), type="PDB")[
        0
    ]
    mol_3 = chimera.openModels.open(os.path.abspath("tests/data/mol3.pdb"), type="PDB")[
        0
    ]

    assert compare.compare_mol(mol_1, mol_2)
    assert not compare.compare_mol(mol_1, mol_3)
    assert not compare.compare_mol(mol_2, mol_3)
