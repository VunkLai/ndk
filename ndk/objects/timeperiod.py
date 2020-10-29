from enum import Enum

from ndk.definitions import timeperiod
from ndk.directives import *


class WEEKDAYS(Enum):
    MONDAY = 'mon'
    TUESDAY = 'tue'
    WEDNESDAY = 'wed'
    THURSDAY = 'thu'
    FRIDAY = 'fri'


class WEEKEND(Enum):
    SUNDAY = 'sun'
    SATURDAY = 'sat'


@attr.s
class TimePeriod(timeperiod.TimePeriodDirective):
    alias = attr.ib(type=str,
                    converter=str,
                    validator=attr.validators.instance_of(str),
                    kw_only=True)

    @alias.default
    def _set_alias_as_timeperiod_name(self):
        return self.timeperiod_name


@attr.s(frozen=True)
class TwentyFourSeven(TimePeriod):
    timeperiod_name = attr.ib(type=str, default='24x7')
    alias = attr.ib(type=str, default='24 hours per day, seven days per week')

    sunday = attr.ib(default='00:00-24:00')
    monday = attr.ib(default='00:00-24:00')
    tuesday = attr.ib(default='00:00-24:00')
    wednesday = attr.ib(default='00:00-24:00')
    thursday = attr.ib(default='00:00-24:00')
    friday = attr.ib(default='00:00-24:00')
    saturday = attr.ib(default='00:00-24:00')


@attr.s(frozen=True)
class BusinessDay(TimePeriod):
    timeperiod_name = attr.ib(type=str, default='8x5')
    alias = attr.ib(type=str, default='8 hours per day, from monday to friday')

    monday = attr.ib(default='08:00-17:00')
    tuesday = attr.ib(default='08:00-17:00')
    wednesday = attr.ib(default='08:00-17:00')
    thursday = attr.ib(default='08:00-17:00')
    friday = attr.ib(default='08:00-17:00')
