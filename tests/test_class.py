import sys
import os

sys.path.insert(0, "/home/travis/miniconda/lib/python2.7/site-packages")

# ESTO COMO HACERLO BIEN PARA NO CAMBIARLO PARA TRAVIS

from pychimera import patch_environ, enable_chimera

patch_environ(nogui=True)
# enable_chimera()


from context import compare
import chimera


class Test_Compare(object):
    def test_pdb(self):
        """Test fot the function compare_pdb"""

        assert compare.compare_pdb("tests/data/mol1", "tests/data/mol2")
        assert not compare.compare_pdb("tests/data/mol1", "tests/data/mol3")
        assert not compare.compare_pdb("tests/data/mol2", "tests/data/mol3")

    def test_mol(self):
        """Test fot the function compare_mol"""

        path = os.path.dirname(os.path.abspath(__file__))
        mol1 = chimera.openModels.open(os.path.join(path, "data/mol1.pdb"), type="PDB")[
            0
        ]
        mol2 = chimera.openModels.open(os.path.join(path, "data/mol2.pdb"), type="PDB")[
            0
        ]
        mol3 = chimera.openModels.open(os.path.join(path, "data/mol3.pdb"), type="PDB")[
            0
        ]

        assert compare.compare_mol(mol1, mol2)
        assert not compare.compare_mol(mol1, mol3)
        assert not compare.compare_mol(mol2, mol3)
