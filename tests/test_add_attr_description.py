import logging
import pytest
import typing
import attr
import cattr

import math
from functools import reduce
from attr_descriptions import *

@attr.s
class C(object):
    x = add_attr_description(attr.ib(default=99), description='description for x')
    y = add_attr_description(attr.ib(default=99), description='description for y')

def test_get_attr_description():
    x_des = get_attr_description(C, 'x')
    assert(x_des =='description for x')
    y_des = get_attr_description(C, 'y')
    assert(y_des =='description for y')
    with pytest.raises(KeyError):
        get_attr_description(C, 'z')



