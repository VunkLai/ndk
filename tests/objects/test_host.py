import unittest

from ndk import core, objects
from ndk.objects import Host, HostConstruct


class HostTestCase(unittest.TestCase):

    def test_L1_construct_is_works(self):
        stack = core.Stack('HostTesting')
        _24x7 = objects.TwentyFourSeven(stack)
        cmd = objects.command.Ping(stack)  # fake cmd
        host = HostConstruct(
            stack, host_name='foo', alias='bar', address='127.0.0.1',
            max_check_attempts=3, check_period=5, notification_interval=60,
            notification_period=_24x7, check_command=cmd)
        assert host.host_name == 'foo'
        assert host.max_check_attempts == 3
        assert host.address == '127.0.0.1'

    def test_L2_construct_is_works(self):
        stack = core.Stack('HostTesting')
        _24x7 = objects.TwentyFourSeven(stack)
        cmd = objects.command.Ping(stack)  # fake cmd
        host = Host(stack, host_name='foo', address='localhost',
                    notification_period=_24x7, check_command=cmd)
        assert host.max_check_attempts == 5
        assert host.address == 'localhost'
