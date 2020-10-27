from enum import Enum

import attr

from ndk.stack import Stack


@attr.s
class Construct(object):
    """A base class of Nagios Objects."""

    __object_type__ = 'template'
    stack = attr.ib(type=Stack,
                    converter=Stack.singleton,
                    validator=attr.validators.instance_of(Stack))

    def __attrs_post_init__(self):
        self.stack.push(self)

    @property
    def pk(self):
        return 'template'

    @property
    def prefix(self):
        return 'define %s {' % self.__object_type__

    @property
    def suffix(self):
        return '}'

    def synth(self):
        return "\n".join(self.__iter__())

    def __iter__(self):
        yield self.prefix
        # self.__dict__ has only attributes that created by attr.ib()
        for name, value in self.__dict__.items():
            if name == 'stack' or value is None:
                continue
            if isinstance(value, bool):
                value = 1 if value else 0
            if isinstance(value, list):
                if isinstance(value[0], Enum):
                    value = ','.join([v.value for v in value])
                else:
                    value = ','.join([v for v in value])
            yield f'    {name}    {value}'
        yield self.suffix

    def __str__(self):
        return self.pk
