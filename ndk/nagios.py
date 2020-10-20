from ndk.core import Stack
from ndk.fields import Field
from ndk.exceptions import IntegrityError


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
                object_type = parents.__object_type__
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
        super().__init__(stack, *args, **kwargs)
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
