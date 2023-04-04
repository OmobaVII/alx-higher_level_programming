#!/usr/bin/python3
"""
this is the 101-locked_class module
it provides the class LockedClass
"""


class LockedClass:
    """defines a class that prevents other classes aside first_name"""
    __slots__ = ("first_name",)

    def __setattr__(self, name, value):
        if not hasattr(self, name) and name != "first_name":
            message = f"'LockedClass' object has no attribute '{name}'"
            raise AttributeError(message)
        super().__setattr__(name, value)
