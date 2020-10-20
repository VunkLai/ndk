from collections import defaultdict

from ndk import exceptions


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

    def push(self, obj):
        """Push a new Nagios Object to this stack.

        Args:
            obj (NagiosObject): The base class of Nagios.
        """
        if obj.pk in self.objects[obj.type]:
            raise exceptions.DuplicateError(
                f'{obj.pk} already exist in {obj.type} objects')
        self.objects[obj.type][obj.pk] = obj
