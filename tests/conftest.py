#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pychimera import patch_environ, enable_chimera

patch_environ()
enable_chimera()

import os
import chimera

TESTPATH = os.path.dirname(os.path.abspath(__file__))


def datapath(path):
    return os.path.join(TESTPATH, "data", path)
