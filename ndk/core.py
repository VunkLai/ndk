from collections import defaultdict

from ndk.exceptions import DuplicateError, IntegrityError
from ndk.fields import Field


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
        if obj.pk in self.objects[obj.__object_type__]:
            raise DuplicateError(
                f'{obj.pk} already exist in {obj.__object_type__} objects')
        self.objects[obj.__object_type__][obj.pk] = obj


class ObjectMeta(type):
    """A metacalss for Nagios Object."""

    def __new__(mcls, name, bases, attrs):
        parents = [b for b in bases if isinstance(b, ObjectMeta)]
        if not parents:
            # Make sure to initialize only the subclasses of Object
            return type.__new__(mcls, name, bases, attrs)

        # parent attrs
        object_type = None
        object_attr = {}
        for parent in parents:
            if hasattr(parent, '__object_type__'):
                object_type = parent.__object_type__
            if hasattr(parent, '__mappings__'):
                object_attr.update(**parent.__mappings__)

        # create __object_type__
        try:
            attrs['__object_type__'] = attrs['Meta'].object_type
        except KeyError:
            attrs['__object_type__'] = object_type

        # create __mappings__
        object_attr.update(**attrs)
        mappings = {k: v for k, v in object_attr.items()
                    if isinstance(v, Field)}
        attrs['__mappings__'] = mappings

        # create __primary_key__
        primary_key = [k for k, v in mappings.items() if v.primary_key]
        attrs['__primary_key__'] = primary_key

        # create __composite_key__
        composite_key = [k for k, v in mappings.items() if v.composite_key]
        attrs['__composite_key__'] = composite_key

        # clean
        for directive in attrs['__mappings__'].keys():
            attrs.pop(directive, None)

        # validation
        if not attrs['__object_type__']:
            raise IntegrityError(f'`__object_type__` not Found: {name}')
        if not attrs['__mappings__']:
            raise IntegrityError(f'`__mappings__` not Found: {name}')
        if not attrs['__primary_key__']:
            raise IntegrityError(f'`__primary_key__` not Found: {name}')

        return super().__new__(mcls, name, bases, attrs)


class Object(dict, metaclass=ObjectMeta):
    """A base class of Nagios Object."""

    def __init__(self, stack, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert isinstance(stack, Stack), f'Stack is invalid: {stack}'
        for key, val in kwargs.items():
            setattr(self, key, val)
        stack.push(self)

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        assert key in self.__mappings__, f'Field name is invalid: {key}'
        self[key] = value

    @property
    def pk(self):
        pks = (Field.normalize_name(self[key]) for key in self.__primary_key__)
        return "::".join(pks)

    def is_valud(self):
        for key, field in self.__mappings__.items():
            if field.required and not any([self.get(key), field.default]):
                raise IntegrityError(
                    f'{key} field is required in {self.__class__.__qualname__}')
