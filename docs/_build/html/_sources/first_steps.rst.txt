First steps
=====================

------------------
How to install
------------------

For the installation, firstly you will need to install UCSF Chimera. Dowlonad the `latest vesion  <http://www.cgl.ucsf.edu/chimera/download.html>`_ and install it with the next command:

.. code-block:: console

    $ chmod +x chimera-*.bin && sudo ./chimera-*.bin
      
Install ``compare_equal`` via the package installer ``pip`` for Python 2.7:

.. code-block:: console

    $ pip install -i https://test.pypi.org/simple/ compare-equal

After the installation you need to add the path where the package is installed (``$PATH_TO_LIB``) 
into the Chimera third-party plugin location library in Preferences. With these commands you
can obtain the path and save it in Chimera Preferences:

.. code-block:: console

    $ PATH_TO_LIB=$(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
    $ chimera --nogui --script <(echo "import chimera; chimera.extension.manager.addDirectory(\"${PATH_TO_LIB}\",True); chimera.preferences.makeCurrentSaved(\"Tools\"); chimera.preferences.save();")

Now you can use the functions for your Python scripts for Chimera.

--------------
How to use it
--------------

Compare Equal package is intended to be used in Python scripts that are going to be run inside of Chimera or in the command line with the ``chimera --nogui`` command. 

The functions are stored in the module ``compare`` inside of the ``compare_equal`` package. However, you can call these functions importing only the package without the module:

.. code-block:: python

    >>> import chimera
    >>> test_1 = chimera.openModels.open("4uft",type="PDB")[0]
    >>> test_2 = chimera.openModels.open("4uft",type="PDB")[0]

    # Without importing the module explicitly
    >>> import compare_equal
    >>> compare_equal.CompareMol(test_1,test_2)
    True

    # Importing the module inside the package explicitly
    >>> from compare_equal import compare
    >>> compare.CompareMol(test_1,test_2)
    True

    # Additionally, you can import only the function that you want
    >>> from compare_equal.compare import CompareMol
    >>> CompareMol(test_1,test_2)
    True

You can use it also interactivily within the Interpreter of `PyChimera <https://pychimera.readthedocs.io/en/latest/>`_.

-----
Tests
-----

This package, has also a subpackage ``tests`` with two tests to check if both functions run as intended. You can run both tests with Chimera in the command line:

.. code-block:: console

    $ chimera --nogui --silent --script <(echo "import compare_equal.tests.mol_test")
    $ chimera --nogui --silent --script <(echo "import compare_equal.tests.pdb_test")

Alternatively, you can run the tests with PyChimera in a simpler way:

.. code-block:: console

    $ pychimera -m compare_equal.tests.mol_test
    $ pychimera -m compare_equal.tests.pdb_test

Both tests are expected to produce no output.
