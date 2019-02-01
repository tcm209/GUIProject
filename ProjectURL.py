# -*- coding: utf-8 -*-
import os
import sys
def _get_project_dir():
    dir = os.path.realpath(sys.argv[0])
    project_dir = os.path.dirname(os.path.abspath(dir))
    # project_dir = os.path.dirname(os.path.abspath(__file__))
    return project_dir
