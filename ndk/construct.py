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
            if name == 'stack':
                continue
            if value is not None:
                yield f'    {name}    {value}'
        yield self.suffix


@attr.s
class TimePeriodConstruct(Construct):
    __object_type__ = 'timeperiod'
    timeperiod_name = attr.ib(type=str, converter=str)
    alias = attr.ib(type=str)

    @property
    def pk(self):
        return self.timeperiod_name
