from importlib import import_module

import attr
from attr import converters
from attr import ib as field

from ndk.construct import Construct


class Converters:
    STR = converters.optional(str)
    INT = converters.optional(int)
    BOOL = converters.optional(bool)

    @staticmethod
    def PrimaryKey(name):
        return str(name).lower().replace(' ', '-')


def PrimaryKey():
    return field(type=str, converter=Converters.PrimaryKey)


def StringField(required=False):
    if required:
        return field(type=str, converter=str, kw_only=True)
    return field(
        type=str, converter=Converters.STR, default=None, kw_only=True)


def IntegerField(required=False):
    if required:
        return field(type=int, converter=int, kw_only=True)
    return field(
        type=int, converter=Converters.INT, default=None, kw_only=True)


def BooleanField(required=False):
    if required:
        return field(type=bool, converter=bool, kw_only=True)
    return field(
        type=bool, converter=Converters.BOOL, default=None, kw_only=True)


def ForeignKey(relation, required=False):
    cls = relation
    if isinstance(relation, str):
        module = import_module('.definitions', package='ndk')
        cls = getattr(module,  f'{relation}Directive')

    if required:
        field(
            type=cls, converter=cls.converter,
            validator=attr.validators.instance_of(cls),
            kw_only=True)
    return field(type=cls, converter=cls.converter,
                 validator=attr.validators.optional(
                     attr.validators.instance_of(cls)),
                 default=None, kw_only=True)


@attr.s
class CommandDirective(Construct):
    __object_type__ = 'command'

    command_name = PrimaryKey()
    command_line = StringField(required=True)

    @property
    def pk(self):
        return self.command_name


@attr.s
class TimePeriodDirective(Construct):
    __object_type__ = 'timeperiod'

    timeperiod_name = PrimaryKey()
    alias = StringField(required=True)
    sunday = StringField()
    monday = StringField()
    tuesday = StringField()
    wednesday = StringField()
    thursday = StringField()
    friday = StringField()
    saturday = StringField()

    @property
    def pk(self):
        return self.timeperiod_name


@attr.s
class ContactDirective(Construct):
    __object_type__ = 'contact'

    contact_name = PrimaryKey()
    alias = StringField()
    # contactgroups = fields.ForeignKey(relation='ContactGroup')
    minimum_importance = IntegerField()
    host_notifications_enabled = BooleanField(required=True)
    service_notifications_enabled = BooleanField(required=True)
    host_notifications_period = ForeignKey(
        'TimePeriod', required=True)
    service_notifications_period = ForeignKey(
        'TimePeriod', required=True)
    # host_notifications_options = fields.ChoiceField(
    #     choices=HostNotifications, required=True)
    # service_notifications_options = fields.ChoiceField(
    #     choices=ServiceNotifications, required=True)
    host_notification_commands = ForeignKey('Command', required=True)
    service_notification_commands = ForeignKey('Command', required=True)
    email = StringField()
    pager = StringField()
    addressx = StringField()
    can_submit_commands = BooleanField()
    retain_status_information = BooleanField()
    retain_nonstatus_information = BooleanField()

    @property
    def pk(self):
        return self.contact_name
