import typing
from enum import Enum
from importlib import import_module

import attr
from attr import converters, validators

from ndk.construct import Construct
from ndk.directives import *


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


class HostNotifications(Enum):
    """
    This directive is used to define the host states for
    which notifications can be sent out to this contact.

    Valid options:
        - d = notify on DOWN host states
        - u = notify on UNREACHABLE host states
        - r = notify on host recoveries (UP states)
        - f = notify when the host starts and stops flapping
        - s = notify when host scheduled downtime starts and ends
        - n = the contact will not receive any type of host notifications
    """

    DOWN = 'd'
    UNREACHABLE = 'u'
    RECOVERY = 'r'
    FLAPPING = 'f'
    SCHEDULED = 's'
    NO = 'n'

    @classmethod
    def choices(cls):
        for name, member in cls.__members__.items():
            if not name == 'NO':
                yield member

    @classmethod
    def all(cls):
        return list(cls.choices())

    @classmethod
    def empty(cls):
        return [cls.NO]


ServiceNotifications = HostNotifications


@attr.s
class ContactGroupDirective(Construct):
    __object_type__ = 'contactgroup'

    contactgroup_name = PrimaryKey()


@attr.s
class ContactDirective(Construct):
    __object_type__ = 'contact'

    contact_name = PrimaryKey()
    alias = StringField()
    contactgroups = ForeignKey('ContactGroup')
    minimum_importance = IntegerField()
    host_notifications_enabled = BooleanField(required=True)
    service_notifications_enabled = BooleanField(required=True)
    host_notifications_period = ForeignKey(
        'TimePeriod', required=True)
    service_notifications_period = ForeignKey(
        'TimePeriod', required=True)
    host_notifications_options = ChoiceField(
        HostNotifications, required=True)
    service_notifications_options = ChoiceField(
        ServiceNotifications, required=True)
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
