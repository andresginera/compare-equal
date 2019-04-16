#!/usr/bin/env python
# -*- coding: utf-8 -*-

from chimera import openModels
from compare_equal import compare
from conftest import datapath


def test_pdb():
    """Test for the function compare_pdb"""

    assert compare.compare_pdb(datapath("mol1"), datapath("mol2"))
    assert not compare.compare_pdb(datapath("mol1"), datapath("mol3"))
    assert not compare.compare_pdb(datapath("mol2"), datapath("mol3"))


def test_mol():
    """Test for the function compare_mol"""

    mol_1 = openModels.open(datapath("mol1.pdb"), type="PDB")[0]
    mol_2 = openModels.open(datapath("mol2.pdb"), type="PDB")[0]
    mol_3 = openModels.open(datapath("mol3.pdb"), type="PDB")[0]

    assert compare.compare_mol(mol_1, mol_2)
    assert not compare.compare_mol(mol_1, mol_3)
    assert not compare.compare_mol(mol_2, mol_3)
