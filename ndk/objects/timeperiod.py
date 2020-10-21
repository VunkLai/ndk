from enum import Enum

from ndk import fields, core


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
    """

    class Meta:
        object_type = 'timeperiod'

    timeperiod_name = fields.StringField(primary_key=True, requried=True)
    alias = fields.StringField(requried=True)
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
    """

    def __init__(self, stack, timeperiod_name, alias=None, **kwargs):
        """
        Define TimePeriod of Nagios Object

        Note:
        `.alias` is requried
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
    """

    timeperiod_name = fields.StringField(
        primary_key=True, requried=True, default='24x7')
    alias = fields.StringField(requried=True, default='24x7')
    sunday = fields.StringField(default='00:00-24:00')
    monday = fields.StringField(default='00:00-24:00')
    tuesday = fields.StringField(default='00:00-24:00')
    wednesday = fields.StringField(default='00:00-24:00')
    thursday = fields.StringField(default='00:00-24:00')
    friday = fields.StringField(default='00:00-24:00')
    saturday = fields.StringField(default='00:00-24:00')

    def __init__(self, stack, **kwargs):
        """
        Define 24x7 TimePeriod of Nagios Object

        TwentyFourSeven means Sunday through Saturday from 00:00 to 24:00.
        """
        super().__init__(stack, **kwargs)


class BusinessDay(TimePeriod):
    """
    L3 Construct: Nagios::Object::TimePeriod
    """
    timeperiod_name = fields.StringField(
        primary_key=True, requried=True, default='8x5')
    alias = fields.StringField(requried=True, default='8x5')
    monday = fields.StringField(default='08:00-17:00')
    tuesday = fields.StringField(default='08:00-17:00')
    wednesday = fields.StringField(default='08:00-17:00')
    thursday = fields.StringField(default='08:00-17:00')
    friday = fields.StringField(default='08:00-17:00')

    def __init__(self, stack, **kwargs):
        """
        Define 8x5 TimePeriod of Nagios Object

        A business day means Monday through Friday from 8 a.m. to 5 p.m..
        """
        super().__init__(stack, **kwargs)
