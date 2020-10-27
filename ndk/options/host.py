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
        return cls.NO


class InitialState(ChoiceMixin, Enum):
    """
    Override the initial state for a Host

    By default Nagios will assume that all hosts are in UP states when it starts.
    You can override the initial state for a host by using this directive.

    Valid options:
        - o = UP
        - d = DOWN
        - u = UNREACHABLE
    """

    UP = 'o'
    DOWN = 'd'
    UNREACHABLE = 'u'


class FlapDetection(ChoiceMixin, Enum):
    """
    This directive is used to determine what host states the flap detection logic will use for this host.

    Valid options:
        - o = UP
        - d = DOWN
        - u = UNREACHABLE
    """

    UP = 'o'
    DOWN = 'd'
    UNREACHABLE = 'u'


class Notification(ChoiceMixin, Enum):
    """
    This directive is used to determine when notifications for the host should be sent out.

    If you do not specify any notification options, Nagios will assume that you want notifications to be sent out for all possible states.

    Valid options:
        - d = send notifications on a DOWN state
        - u = send notifications on an UNREACHABLE state
        - r = send notifications on recoveries (OK state)
        - f = send notifications when the host starts and stops flapping
        - s = send notifications when scheduled downtime starts and ends
        - n = no host notifications will be sent out
    """

    DOWN = 'd'
    UNREACHABLE = 'u'
    RECOVERY = 'r'
    FLAPPING = 'f'
    SCHEDULED = 's'
    NO = 'n'


class Stalking(ChoiceMixin, Enum):
    """
    This directive determines which host states "stalking" is enabled for.

    Note: As of Core 4.4.0 you can use the N option to log event states when notifications are sent out.

    Valid options:
        - o = stalk on UP states
        - d = stalk on DOWN states
        - u = stalk on UNREACHABLE states
    """

    UP = 'o'
    DOWN = 'd'
    UNREACHABLE = 'u'
