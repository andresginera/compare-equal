import sys
import os

sys.path.insert(0, "/home/travis/miniconda/lib/python2.7/site-packages")

# I need to resolve this to not change it for travis and local use

from pychimera import patch_environ, enable_chimera

patch_environ()
# enable_chimera()

import chimera
from context import compare


class Test_Compare(object):
    """Class for the tests with pytest"""


    def test_pdb(self):
        """Test fot the function compare_pdb"""

        assert compare.compare_pdb("tests/data/mol1", "tests/data/mol2")
        assert not compare.compare_pdb("tests/data/mol1", "tests/data/mol3")
        assert not compare.compare_pdb("tests/data/mol2", "tests/data/mol3")

    def test_mol(self):
        """Test fot the function compare_mol"""

        path = os.path.dirname(os.path.abspath(__file__))
        mol_1 = chimera.openModels.open(
            os.path.join(path, "data/mol1.pdb"), type="PDB"
        )[0]
        mol_2 = chimera.openModels.open(
            os.path.join(path, "data/mol2.pdb"), type="PDB"
        )[0]
        mol_3 = chimera.openModels.open(
            os.path.join(path, "data/mol3.pdb"), type="PDB"
        )[0]

        assert compare.compare_mol(mol_1, mol_2)
        assert not compare.compare_mol(mol_1, mol_3)
        assert not compare.compare_mol(mol_2, mol_3)
