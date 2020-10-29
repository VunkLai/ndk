import unittest

from ndk.objects.command import Email, Ping
from ndk.objects.host import Host
from ndk.objects.service import Service
from ndk.objects.timeperiod import TwentyFourSeven
from ndk.options import service as options
from ndk.stack import Stack


class ServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack('ServiceTesting')
        self.tp = TwentyFourSeven(self.stack)
        self.cmd = Email(self.stack)

    def test_service(self):
        host = Host(
            self.stack, host_name='foo', check_period=self.tp,
            notification_period=self.tp)
        ping = Ping(self.stack)
        assert Service(
            self.stack, host_name=host, service_description='bar',
            check_command=ping, notification_period=self.tp)

    def test_pk(self):
        host = Host(
            self.stack, host_name='foo', check_period=self.tp,
            notification_period=self.tp)
        ping = Ping(self.stack)
        srv = Service(
            self.stack, host_name=host, service_description='bar',
            check_command=ping, notification_period=self.tp)
        assert srv.pk == 'foo::bar'
