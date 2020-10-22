import unittest

from ndk import core, objects
from ndk.objects import (BusinessDay, TimePeriod, TimePeriodConstruct,
                         TwentyFourSeven)


class TimePeriodTestCase(unittest.TestCase):

    def test_L1_construct_is_works(self):
        stack = core.Stack('TimePeriodTesting')
        tp = TimePeriodConstruct(
            stack, timeperiod_name='foo', alias='bar', sunday='00:00-24:00')
        assert tp.pk == 'foo'
        assert tp.alias == 'bar'
        assert tp.sunday == '00:00-24:00'

    def test_L2_construct_is_works(self):
        stack = core.Stack('TimePeriodTesting')
        tp = TimePeriod(
            stack, timeperiod_name='foo', alias='bar', monday='00:00-24:00')
        assert tp.sunday is None
        assert tp.monday == '00:00-24:00'

    def test_twenty_four_seven_is_works(self):
        stack = core.Stack('TimePeriodTesting')
        tp = TwentyFourSeven(stack)
        assert tp.pk == '24x7'
        assert tp.sunday == '00:00-24:00'
        assert all([tp.sunday, tp.monday, tp.tuesday, tp.wednesday,
                    tp.thursday, tp.friday, tp.saturday])

        tp = BusinessDay(stack)
        assert tp.pk == '8x5'
        assert tp.monday == '08:00-17:00'
        assert all([tp.monday, tp.tuesday, tp.wednesday,
                    tp.thursday, tp.friday])
