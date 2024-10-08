#!/usr/bin/python3
"""Define a locked class."""

class LockedClass:
   """
   prevent the user from instantiating new LockClass attributes
   for anything but attributes called 'first_name'.

   __slot__ = ["first_name"]
