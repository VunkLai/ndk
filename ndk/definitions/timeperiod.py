import attr
from ndk.construct import Construct
from ndk.directives import *


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
