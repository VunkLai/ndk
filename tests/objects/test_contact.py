import unittest

from ndk import core, objects
from ndk.objects import Contact, ContactConstruct
from ndk.objects.contact import HostNotifications, ServiceNotifications


class ContactTestCase(unittest.TestCase):

    def test_constructs_are_works(self):
        stack = core.Stack('ContactTesting')
        _24x7 = objects.TwentyFourSeven(stack)
        cmd = objects.command.Ping(stack)  # fake cmd
        contact = ContactConstruct(
            stack, contact_name='foo',
            host_notifications_enabled=True,
            service_notifications_enabled=True,
            host_notifications_period=_24x7,
            service_notifications_period=_24x7,
            host_notifications_options=HostNotifications.all(),
            service_notifications_options=ServiceNotifications.all(),
            host_notification_commands=cmd,
            service_notification_commands=cmd)
        assert contact.contact_name == 'foo'

        contact = Contact(
            stack, contact_name='bar',
            host_notifications_period=_24x7,
            service_notifications_period=_24x7,
            host_notification_commands=cmd,
            service_notification_commands=cmd)
        assert contact.host_notifications_enabled == True
        assert contact.host_notifications_options == ['d', 'u', 'r', 'f', 's']

    def test_L3_construct_is_works(self):
        stack = core.Stack('ContactTesting')
        _24x7 = objects.TwentyFourSeven(stack)
        cmd = objects.command.Ping(stack)  # fake cmd
        contact = objects.contact.Email(
            stack, contact_name='bar', email='foo@bar.baz',
            host_notifications_period=_24x7,
            service_notifications_period=_24x7,
            host_notification_commands=cmd,
            service_notification_commands=cmd)
        assert contact.host_notifications_enabled == True
        assert contact.host_notifications_options == ['d', 'u', 'r', 'f', 's']
        assert contact.email == 'foo@bar.baz'
