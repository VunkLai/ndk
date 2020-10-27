import unittest

from ndk import core, objects
from ndk.objects import Service, ServiceConstruct


class ServiceTestCase(unittest.TestCase):

    @unittest.skip('skip, the code is merging')
    def test_L1_construct_is_works(self):
        stack = core.Stack('ServiceTesting')
        _24x7 = objects.TwentyFourSeven(stack)
        cmd = objects.command.Ping(stack)  # fake cmd
        service = ServiceConstruct(
            stack, service_description='foo', host_name='bar',
            check_command=cmd, check_interval=5, retry_interval=1,
            check_period=_24x7, notification_interval=60,
            notification_period=_24x7)
        assert service.service_description == 'foo'

    def test_L2_construct_is_works(self):
        stack = core.Stack('ServiceTesting')
        service = Service(
            stack, service_description='foo', host_name='foo',
            check_command='asdf', notification_period='24x7')
        assert service.max_check_attempts == 5
