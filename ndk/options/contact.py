from enum import Enum


class ChoiceMixin:

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


class HostNotifications(ChoiceMixin, Enum):
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


class ServiceNotifications(ChoiceMixin, Enum):
    """
    This directive is used to define the service states for
    which notifications can be sent out to this contact.

    Valid options:
        - w = notify on WARNING service states
        - u = notify on UNKNOWN service states
        - c = notify on CRITICAL service states
        - r = notify on service recoveries (OK states)
        - f = notify when the service starts and stops flapping
        - n = the contact will not receive any type of service notifications.
    """

    WARNING = 'w'
    UNKNOWN = 'u'
    CRITICAL = 'c'
    RECOVERY = 'r'
    FLAPPING = 'f'
    SCHEDULED = 's'
    NO = 'n'
