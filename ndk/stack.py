from collections import defaultdict
# from ndk import construct
from importlib import import_module

import attr


class Stack:
    """A NDK stack.
    """

    def __init__(self, name):
        """Initialize a NDK stack.

        Args:
            name (str): the application name.
        """
        self.name = name
        self.objects = defaultdict(dict)

    def __iter__(self):
        """Iter all objects.

        Yields:
            obj (NagiosObject): the next obj in the range of the all objects.
        """
        for obj in self.objects.values():
            yield from obj.values()

    @classmethod
    def singleton(cls, stack):
        if isinstance(stack, cls):
            return stack
        return cls(stack)

    def push(self, obj):
        """Push a new Nagios Object to this stack.

        Args:
            obj (NagiosObject): The base class of Nagios.
        """
        construct = import_module('.construct', package='ndk')
        assert isinstance(
            obj, construct.Construct), f'{obj} must be Construct instance'
        self.objects[obj.__object_type__][obj.pk] = obj

    def synth(self):
        """Synthesizes the Nagios objects for this stack"""
        return '\n'.join((obj.synth() for obj in self))
