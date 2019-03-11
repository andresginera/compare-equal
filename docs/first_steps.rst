First steps
=====================

This is the documentation for the package Compare-Equal.

------------------
How to install
------------------

For the installation, firstly you will need to install UCSF Chimera. Dowlonad the `lastest vesion  <http://www.cgl.ucsf.edu/chimera/download.html>`_ and install it with the next command:

.. code-block:: bash

    $ chmod +x chimera-*.bin && sudo ./chimera-*.bin
      
Install ``compare_equal`` via the package installer ``pip`` for Python 2.7:

.. code-block:: bash

    $ pip install -i https://test.pypi.org/simple/ compare-equal

After the installation you need to add the path where the package is installed (``$PATH``) into the Chimera third-party plugin location library in Preferences. You need to substitute ``$PATH`` with your absolute path:

.. code-block:: bash

    $ chimera --nogui --script <(echo "import chimera; chimera.extension.manager.addDirectory(\"${PATH}/lib/python2.7/site-packages\",True); chimera.preferences.makeCurrentSaved(\"Tools\"); chimera.preferences.save();")

Now you can use the functions for your Python scripts for Chimera.

--------------
How to use it
--------------

Compare-Equal package is intended to be used in Python scripts that are going to be run inside of Chimera or in the command line with the ``chimera --nogui`` command. 

Although, you can use it also interactivily with Chimera as an interpreter, you can also import the package within the Interpreter of `PyChimera <https://pychimera.readthedocs.io/en/latest/>`_.

-----
Tests
-----

This package, has a subpackage ``tests`` with two tests to check if both functions run as intended. You can run both tests with Chimera in the command line:

.. code-block:: bash

    $ chimera --nogui --silent --script <(echo "import compare_equal.tests.mol_test")
    $ chimera --nogui --silent --script <(echo "import compare_equal.tests.pdb_test")

Alternatively, you can run the tests with PyChimera in a simpler way:

.. code-block:: bash

    $ pychimera -m compare_equal.tests.mol_test
    $ pychimera -m compare_equal.tests.pdb_test

Both tests are expected to produce no output.