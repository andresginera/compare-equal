Documentation for developers
=============================

In this section you have the source code for each of the function and tests.

----------
Functions
----------

Comparison of two PDB files
****************************

.. literalinclude:: ../compare_equal/compare.py
    :language: python
    :lines: 13-42


Comparison of two Python variables
***********************************

.. literalinclude:: ../compare_equal/compare.py
    :language: python
    :lines: 45-78

---------------
Tests
---------------

Path provider function
***************************

.. literalinclude:: ../tests/conftest.py
    :language: python
    :lines: 6-10

Test for compare_pdb
*********************************************

.. literalinclude:: ../tests/test_compare.py
    :language: python
    :lines: 16-21

Test for compare_mol
*********************************************

.. literalinclude:: ../tests/test_compare.py
    :language: python
    :lines: 24-33