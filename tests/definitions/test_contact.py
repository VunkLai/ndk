import unittest

from ndk.definitions import (CommandDirective, ContactDirective,
                             TimePeriodDirective)
from ndk.stack import Stack


class ContactDirectiveTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack('ContactTesting')
        self.tp = TimePeriodDirective(
            self.stack, timeperiod_name='24x7', alias='foo')
        self.cmd = CommandDirective(
            self.stack, command_name='email', command_line='bar')
        self.requried_directive = dict(
            contact_name='Foo Bar',
            host_notifications_enabled=True,
            service_notifications_enabled=True,
            host_notifications_period=self.tp,
            service_notifications_period=self.tp,
            host_notification_commands=self.cmd,
            service_notification_commands=self.cmd
        )

    def test_contact_directive(self):
        with self.assertRaises(TypeError):
            ContactDirective(self.stack)
        assert ContactDirective(self.stack, **self.requried_directive)

    def test_pk_and_name(self):
        self.requried_directive.pop('contact_name')
        with self.assertRaises(TypeError):
            ContactDirective(self.stack, **self.requried_directive)

        self.requried_directive['contact_name'] = 'Foo Bar'
        contact = ContactDirective(self.stack, **self.requried_directive)
        assert contact.pk == 'foo-bar'
        assert contact.contact_name == 'foo-bar'

    def test_alias(self):
        contact = ContactDirective(self.stack, **self.requried_directive)
        assert contact.alias is None

        contact = ContactDirective(
            self.stack, alias='Foo Bar', **self.requried_directive)
        assert contact.alias == 'Foo Bar'

    def test_minimum_importance(self):
        contact = ContactDirective(self.stack, **self.requried_directive)
        assert contact.minimum_importance is None

        tp = ContactDirective(
            self.stack, minimum_importance=30, **self.requried_directive)
        assert isinstance(tp.minimum_importance, int)
        assert tp.minimum_importance == 30

    def test_host_notifications_enabled(self):
        contact = ContactDirective(self.stack, **self.requried_directive)
        assert contact.host_notifications_enabled

        self.requried_directive.pop('host_notifications_enabled')
        with self.assertRaises(TypeError):
            ContactDirective(self.stack, **self.requried_directive)

    def test_service_notifications_enabled(self):
        contact = ContactDirective(self.stack, **self.requried_directive)
        assert contact.service_notifications_enabled

        self.requried_directive.pop('service_notifications_enabled')
        with self.assertRaises(TypeError):
            ContactDirective(self.stack, **self.requried_directive)

    def test_host_notifications_period(self):
        contact = ContactDirective(self.stack, **self.requried_directive)
        assert contact.host_notifications_period is self.tp

        self.requried_directive.pop('host_notifications_period')
        with self.assertRaises(TypeError):
            ContactDirective(self.stack, **self.requried_directive)

    def test_service_notifications_period(self):
        contact = ContactDirective(self.stack, **self.requried_directive)
        assert contact.service_notifications_period is self.tp

        self.requried_directive.pop('service_notifications_period')
        with self.assertRaises(TypeError):
            ContactDirective(self.stack, **self.requried_directive)

    def test_host_notification_commands(self):
        contact = ContactDirective(self.stack, **self.requried_directive)
        assert contact.host_notification_commands is self.cmd

        self.requried_directive.pop('host_notification_commands')
        with self.assertRaises(TypeError):
            ContactDirective(self.stack, **self.requried_directive)

    def test_service_notification_commands(self):
        contact = ContactDirective(self.stack, **self.requried_directive)
        assert contact.service_notification_commands is self.cmd

        self.requried_directive.pop('service_notification_commands')
        with self.assertRaises(TypeError):
            ContactDirective(self.stack, **self.requried_directive)

    def test_synth(self):
        contact = ContactDirective(self.stack, **self.requried_directive)
        tmp = (
            'define contact {',
            '    contact_name    foo-bar',
            '    host_notifications_enabled    1',
            '    service_notifications_enabled    1',
            '    host_notifications_period    24x7',
            '    service_notifications_period    24x7',
            '    host_notification_commands    email',
            '    service_notification_commands    email',
            '}')
        assert '\n'.join(tmp) == contact.synth()
