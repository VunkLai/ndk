import unittest

from ndk.definitions import CommandDirective
from ndk.stack import Stack


class CommandDirectiveTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack('commandTesting')

    def test_command_directive(self):
        with self.assertRaises(TypeError):
            CommandDirective(self.stack)
        with self.assertRaises(TypeError):
            CommandDirective(self.stack, command_name='foo')
        with self.assertRaises(TypeError):
            CommandDirective(self.stack, command_line='bar')
        assert CommandDirective(
            self.stack, command_name='foo', command_line='bar')

    def test_command_name(self):
        tp = CommandDirective(
            self.stack, command_name='Foo Bar', command_line='Foo Bar')
        assert tp.pk == 'foo-bar'
        assert tp.command_name == 'foo-bar'

    def test_command_line(self):
        tp = CommandDirective(
            self.stack, command_name='Foo Bar', command_line='Foo Bar')
        assert tp.command_line == 'Foo Bar'

    def test_synth(self):
        tp = CommandDirective(
            self.stack, command_name='Foo Bar', command_line='Foo Bar')
        tmp = (
            'define command {', '    command_name    foo-bar',
            '    command_line    Foo Bar', '}')
        assert '\n'.join(tmp) == tp.synth()
