#!/usr/bin/python3
class LockedClass:
    """A locked class that only allows user to
    create fitst_name attribute"""
    __slots__ = ["first_name"]
