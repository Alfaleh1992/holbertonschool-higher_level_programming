#!/usr/bin/python3
"""
Defines function inherits_from
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is a subclass instance of a_class, not a direct instance.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
