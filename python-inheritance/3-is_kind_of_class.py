#!/usr/bin/python3
"""
Defines function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class or a subclass of it.
    Otherwise return False.
    """
    return isinstance(obj, a_class)
