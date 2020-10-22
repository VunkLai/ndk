from enum import Enum

from ndk import core, fields


class WEEKDAYS(Enum):
    MONDAY = 'mon'
    TUESDAY = 'tue'
    WEDNESDAY = 'wed'
    THURSDAY = 'thu'
    FRIDAY = 'fri'


class WEEKEND(Enum):
    SUNDAY = 'sun'
    SATURDAY = 'sat'


class TimePeriodConstruct(core.Object):
    """
    L1 Construct: Nagios::Object::TimePeriod

    This construct correspond directly to Command defined by Nagios.
    """

    class Meta:
        object_type = 'timeperiod'

    timeperiod_name = fields.StringField(primary_key=True, required=True)
    alias = fields.StringField(required=True)
    sunday = fields.StringField()
    monday = fields.StringField()
    tuesday = fields.StringField()
    wednesday = fields.StringField()
    thursday = fields.StringField()
    friday = fields.StringField()
    saturday = fields.StringField()

    def __init__(self, stack, timeperiod_name, alias,
                 sunday=None, monday=None, tuesday=None, wednesday=None,
                 thursday=None, friday=None, saturday=None):
        super().__init__(stack=stack, timeperiod_name=timeperiod_name,
                         alias=alias, sunday=sunday, monday=monday,
                         tuesday=tuesday, wednesday=wednesday,
                         thursday=thursday, friday=friday, saturday=saturday)


class TimePeriod(TimePeriodConstruct):
    """
    L2 Construct: Nagios::Object::TimePeriod

    Command encapsulate L1 modules, it is developed to address specific use 
    cases and sensible defaults.
    """

    def __init__(self, stack, timeperiod_name, alias=None, **kwargs):
        """
        Define TimePeriod of Nagios Object

        Note:
        `.alias` is required
        If `.alias` is not set, it is the same as the timeperiod_name.
        """
        alias = alias or timeperiod_name
        super().__init__(stack=stack,
                         timeperiod_name=timeperiod_name,
                         alias=alias,
                         **kwargs)


class TwentyFourSeven(TimePeriod):
    """
    L3 Construct: Nagios::Object::TimePeriod

    L3 declare a resource to create particular use cases.
    """

    def __init__(self, stack, timeperiod_name='24x7',
                 alias='twenty-four seven', sunday='00:00-24:00',
                 monday='00:00-24:00', tuesday='00:00-24:00',
                 wednesday='00:00-24:00', thursday='00:00-24:00',
                 friday='00:00-24:00', saturday='00:00-24:00'):
        """
        Define 24x7 TimePeriod of Nagios Object

        TwentyFourSeven means Sunday through Saturday from 00:00 to 24:00.
        """
        super().__init__(stack, timeperiod_name=timeperiod_name, alias=alias,
                         sunday=sunday, monday=monday, tuesday=tuesday, wednesday=wednesday,
                         thursday=thursday, friday=friday, saturday=saturday)


class BusinessDay(TimePeriod):
    """
    L3 Construct: Nagios::Object::TimePeriod

    L3 declare a resource to create particular use cases.
    """

    def __init__(
            self, stack, timeperiod_name='8x5', alias='business day',
            monday='08:00-17:00', tuesday='08:00-17:00',
            wednesday='08:00-17:00', thursday='08:00-17:00',
            friday='08:00-17:00', **kwargs):
        """
        Define 8x5 TimePeriod of Nagios Object

        A business day means Monday through Friday from 8 a.m. to 5 p.m..
        """
        super().__init__(stack, timeperiod_name=timeperiod_name, alias=alias,
                         monday=monday, tuesday=tuesday, wednesday=wednesday,
                         thursday=thursday, friday=friday, **kwargs)
