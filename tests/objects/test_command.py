import unittest

from ndk import core, objects
from ndk.objects import Command, CommandConstruct


class CommandTestCase(unittest.TestCase):

    def test_constructs_are_works(self):
        stack = core.Stack('CommandTesting')
        cmd = CommandConstruct(stack, command_name='top', command_line='top')
        assert cmd.command_name == 'top'

        cmd = Command(stack, command_name='ping',
                      command_line='ping 127.0.0.1')
        assert cmd.command_line == 'ping 127.0.0.1'

    def test_L3_construct_is_works(self):
        stack = core.Stack('CommandTesting')
        cmd = objects.command.Ping(stack, command_name='check-ping')
        assert cmd.command_name == 'check-ping'
        assert 'ping' in cmd.command_line
