import unittest

import attr
from ndk.objects.command import Email as SendByEmail
from ndk.objects.contact import Contact, Email
from ndk.objects.timeperiod import TwentyFourSeven
from ndk.options import contact as options
from ndk.stack import Stack

# import HostNotifications, ServiceNotifications


class ContactTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack('ContactTesting')

    def test_contact(self):
        tp = TwentyFourSeven(self.stack)
        cmd = SendByEmail(self.stack)
        contact = Contact(self.stack, contact_name='foo',
                          host_notifications_period=tp,
                          service_notifications_period=tp,
                          host_notification_commands=cmd,
                          service_notification_commands=cmd)
        assert contact.contact_name == 'foo'
        assert contact.host_notifications_enabled
        assert 'service_notifications_options    w,u,c,r,f,s' in contact.synth()


class EmailTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack('EmailTesting')

    def test_email(self):
        tp = TwentyFourSeven(self.stack)
        cmd = SendByEmail(self.stack)
        with self.assertRaises(TypeError):
            contact = Email(self.stack, contact_name='foo',
                            host_notifications_period=tp,
                            service_notifications_period=tp,
                            host_notification_commands=cmd,
                            service_notification_commands=cmd)
        assert Email(self.stack, contact_name='foo', email='foo@bar.baz',
                     host_notifications_period=tp,
                     service_notifications_period=tp,
                     host_notification_commands=cmd,
                     service_notification_commands=cmd)
