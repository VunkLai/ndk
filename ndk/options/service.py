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

    By default Nagios will assume that all services are in OK states when it starts.
    You can override the initial state for a host by using this directive.

    Valid options:
      - o = OK
      - w = WARNING
      - u = UNKNOWN
      - c = CRITICAL
    """

    OK = 'o'
    WARNING = 'w'
    UNKNOWN = 'u'
    CRITICAL = 'c'


class FlapDetection(ChoiceMixin, Enum):
    """
    This directive is used to determine what service states the flap detection
    logic will use for this service.

    Valid options:
      - o = OK
      - w = WARNING
      - u = UNKNOWN
      - c = CRITICAL
    """

    OK = 'o'
    WARNING = 'w'
    UNKNOWN = 'u'
    CRITICAL = 'c'


class Notification(ChoiceMixin, Enum):
    """
    This directive is used to determine
    when notifications for the service should be sent out.

    If you do not specify any notification options,
    Nagios will assume that you want notifications to be sent out
    for all possible states.

    Valid options:
      - w = send notifications on a WARNING state
      - c = send notifications on a CRITICAL state
      - u = send notifications on an UNKNOWN state
      - r = send notifications on recoveries (OK state)
      - f = send notifications when the service starts and stops flapping
      - s = send notifications when scheduled downtime starts and ends
      - n = no service notifications will be sent out
    """

    WARNING = 'w'
    CRITICAL = 'c'
    UNKNOWN = 'u'
    RECOVERY = 'r'
    FLAPPING = 'f'
    SCHEDULED = 's'
    NO = 'n'


class Stalking(ChoiceMixin, Enum):
    """
    This directive determines which service states "stalking" is enabled for.

    Note: As of Core 4.4.0 you can use the N option to log event states when notifications are sent out.

    Valid options:
      - o = stalk on OK states
      - w = stalk on WARNING states
      - u = stalk on UNKNOWN states
      - c = stalk on CRITICAL states
    """

    OK = 'o'
    WARNING = 'w'
    UNKNOWN = 'u'
    CRITICAL = 'c'
