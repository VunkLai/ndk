import unittest

import attr
from ndk.objects import BusinessDay, TimePeriod, TwentyFourSeven
from ndk.stack import Stack


class TimePeriodTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack('TimePeriodTesting')

    def test_timeperiod(self):
        tp = TimePeriod(self.stack, timeperiod_name='foo')
        assert tp.pk == 'foo'
        assert tp.timeperiod_name == 'foo'
        assert tp.alias == 'foo'

    def test_weekdays(self):
        tp = TimePeriod(
            self.stack, timeperiod_name='foo', monday='00:00-24:00')
        assert tp.sunday is None
        assert tp.monday == '00:00-24:00'


class TwentyFourSevenTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack('TwentyFourSevenTesting')

    def test_twenty_four_seven(self):
        tp = TwentyFourSeven(self.stack)
        assert tp.pk == '24x7'
        assert tp.alias == '24 hours per day, seven days per week'
        for day in [tp.sunday, tp.monday, tp.tuesday, tp.wednesday,
                    tp.thursday, tp.friday, tp.saturday]:
            with self.subTest(day=day):
                assert day == '00:00-24:00'

    def test_frozen(self):
        tp = TwentyFourSeven(self.stack)
        with self.assertRaises(attr.exceptions.FrozenInstanceError):
            tp.timeperiod_name = 'foo'


class BusinessDayTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack('BusinessDayTesting')

    def test_business_day(self):
        tp = BusinessDay(self.stack)
        assert tp.pk == '8x5'
        assert tp.alias == '8 hours per day, from monday to friday'
        for day in [
                tp.monday, tp.tuesday, tp.wednesday, tp.thursday, tp.friday]:
            with self.subTest(day=day):
                assert day == '08:00-17:00'

    def test_frozen(self):
        tp = BusinessDay(self.stack)
        with self.assertRaises(attr.exceptions.FrozenInstanceError):
            tp.timeperiod_name = 'foo'
