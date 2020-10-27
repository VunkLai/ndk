
from enum import Enum

import attr
from ndk.construct import Construct
from ndk.directives import *


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
class ContactDirective(Construct):
    __object_type__ = 'contact'

    contact_name = PrimaryKey()
    alias = StringField()
    contactgroups = OneToMany('ContactGroup')
    minimum_importance = IntegerField()
    host_notifications_enabled = BooleanField(required=True)
    service_notifications_enabled = BooleanField(required=True)
    host_notifications_period = OneToOne(
        'TimePeriod', required=True)
    service_notifications_period = OneToOne(
        'TimePeriod', required=True)
    host_notifications_options = ChoiceField(
        HostNotifications, required=True)
    service_notifications_options = ChoiceField(
        ServiceNotifications, required=True)
    host_notification_commands = OneToOne('Command', required=True)
    service_notification_commands = OneToOne('Command', required=True)
    email = StringField()
    pager = StringField()
    addressx = StringField()
    can_submit_commands = BooleanField()
    retain_status_information = BooleanField()
    retain_nonstatus_information = BooleanField()

    @property
    def pk(self):
        return self.contact_name
