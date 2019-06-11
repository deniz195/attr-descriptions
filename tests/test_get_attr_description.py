import logging

import typing
import attr
import cattr

import math
from functools import reduce
from attr_descriptions import *

@attr.s
class C(object):
    x = add_attr_description(attr.ib(default=99), description='Some parameter')

def test_add_attr_description():
    c = C()
    assert(attr.fields(C).x.metadata['__description']=='Some parameter')



