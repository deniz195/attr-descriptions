import pytest
import logging

import typing
import attr
import cattr

import math
from functools import reduce
from attr_descriptions import *

def test_add_attr_description():
    @attr.s
    class C(object):
        x = add_attr_description(attr.ib(default=99), description='Some parameter')

    c = C()
    assert(attr.fields(C).x.metadata['__description']=='Some parameter')


def test_get_attr_description():
    @attr.s
    class C(object):
        x = add_attr_description(attr.ib(default=99), description='description for x')
        y = add_attr_description(attr.ib(default=99), description='description for y')

    x_des = get_attr_description(C, 'x')
    assert(x_des =='description for x')
    y_des = get_attr_description(C, 'y')
    assert(y_des =='description for y')
    with pytest.raises(KeyError):
        get_attr_description(C, 'z')




def test_describe():
    @attr.s
    class C(object):
        x = describe(attr.ib(default=99), description='description for x', significant_digits=2)
        y = describe(attr.ib(default=99), description='description for y', significant_digits=2)
        z1 = attr.ib(default=99)
        z2 = describe(attr.ib(default=99), description=None)

    x_des = get_attr_description(C, 'x')
    assert(x_des =='description for x')
    y_des = get_attr_description(C, 'y')
    assert(y_des =='description for y')

    x_des = get(C, 'x', 'No description', 3)
    assert(x_des == dict(description='description for x', significant_digits=2))

    z_des = get(C, 'z1', 'No description', 3)
    assert(z_des == dict(description='No description', significant_digits=3))

    z_des = get(C, 'z2', 'No description', 3)
    assert(z_des == dict(description='No description', significant_digits=3))



