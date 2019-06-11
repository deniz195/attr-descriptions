import pytest
import os
from pathlib import Path

#get path to file and construct the dependencies for the db, pint, mvc accordingly
path_fn = os.path.dirname(os.path.abspath(__file__))
path_fn = Path(path_fn)
attr_des   = path_fn.joinpath('..','attr_descriptions')

import sys
sys.path.append('..')
sys.path.insert(0, os.fspath(attr_des))


