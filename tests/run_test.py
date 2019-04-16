#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pychimera import patch_environ, enable_chimera
import sys
import pytest


if __name__ == "__main__":
    patch_environ()
    enable_chimera()
    sys.exit(pytest.main())
