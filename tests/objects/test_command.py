import unittest

import attr
from ndk.objects.command import Command, Email, Ping
from ndk.stack import Stack


class CommandTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack('CommandTesting')

    def test_command(self):
        assert Command(
            self.stack, command_name='top', command_line='top')

    def test_command_name(self):
        with self.assertRaises(TypeError):
            Command(self.stack, command_line='bar')
        cmd = Command(
            self.stack, command_name='foo', command_line='bar')
        assert cmd.command_name == 'foo'

    def test_command_line(self):
        with self.assertRaises(TypeError):
            Command(self.stack, command_name='foo')
        cmd = Command(
            self.stack, command_name='foo', command_line='bar')
        assert cmd.command_line == 'bar'


class PingTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack('PingTesting')

    def test_ping(self):
        assert Ping(self.stack)
        with self.assertRaises(attr.exceptions.FrozenInstanceError):
            cmd = Ping(self.stack)
            cmd.name = 'foo'

    def test_command_name(self):
        cmd = Ping(self.stack)
        assert cmd.command_name == 'ping'

    def test_command_line(self):
        cmd = Ping(self.stack)
        assert 'ping' in cmd.command_line


class EmailTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack('EmailTesting')

    def test_email(self):
        assert Email(self.stack)
        with self.assertRaises(attr.exceptions.FrozenInstanceError):
            cmd = Ping(self.stack)
            cmd.name = 'foo'

    def test_command_name(self):
        cmd = Email(self.stack)
        assert cmd.command_name == 'send-by-email'

    def test_command_line(self):
        cmd = Email(self.stack)
        assert 'smtp' in cmd.command_line
