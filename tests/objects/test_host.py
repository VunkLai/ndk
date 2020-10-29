import unittest

from ndk.objects.command import Email
from ndk.objects.host import Host
from ndk.objects.timeperiod import TwentyFourSeven
from ndk.options import host as options
from ndk.stack import Stack


class HostTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack('HostTesting')
        self.tp = TwentyFourSeven(self.stack)
        self.cmd = Email(self.stack)

    def test_host(self):
        host = Host(self.stack, host_name='Foo Bar',
                    check_period=self.tp, notification_period=self.tp)
        assert host.host_name == 'foo-bar'
        assert host.max_check_attempts == 5
        assert host.check_period.timeperiod_name == '24x7'

    # @unittest.skip('skip, the code is merging')
    # def test_L2_construct_is_works(self):
    #     _24x7 = objects.TwentyFourSeven(self.stack)
    #     cmd = objects.command.Ping(self.stack)  # fake cmd
    #     host = Host(self.stack, host_name='foo', address='localhost',
    #                 notification_period=_24x7, check_period=_24x7,
    #                 check_command=cmd)
    #     assert host.max_check_attempts == 5
    #     assert host.address == 'localhost'
