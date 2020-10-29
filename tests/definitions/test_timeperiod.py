import unittest

from ndk.definitions import TimePeriodDirective
from ndk.stack import Stack


class TimePeriodDirectiveTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack('TimePeriodDirectiveTesting')

    def test_timeperiod_directive(self):
        with self.assertRaises(TypeError):
            TimePeriodDirective(self.stack)
        with self.assertRaises(TypeError):
            TimePeriodDirective(self.stack, timeperiod_name='foo')
        with self.assertRaises(TypeError):
            TimePeriodDirective(self.stack, alias='bar')
        assert TimePeriodDirective(
            self.stack, timeperiod_name='foo', alias='bar')

    def test_name(self):
        tp = TimePeriodDirective(
            self.stack, timeperiod_name='Foo Bar', alias='Foo Bar')
        assert tp.pk == 'foo-bar'
        assert tp.timeperiod_name == 'foo-bar'
        assert tp.alias == 'Foo Bar'

    def test_periods(self):
        tp = TimePeriodDirective(
            self.stack, timeperiod_name='Foo Bar', alias='Foo Bar',
            sunday='00:00-24:00')
        assert tp.sunday == '00:00-24:00'

    def test_synth(self):
        tp = TimePeriodDirective(
            self.stack, timeperiod_name='Foo Bar', alias='Foo Bar',
            sunday='00:00-24:00', monday='08:00-17:00')
        assert tp.monday == '08:00-17:00'
        tmp = (
            'define timeperiod {', '    timeperiod_name    foo-bar',
            '    alias    Foo Bar', '    sunday    00:00-24:00',
            '    monday    08:00-17:00', '}')
        assert '\n'.join(tmp) == tp.synth()
