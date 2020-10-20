import unittest

from ndk import core
from ndk import exceptions


class StackTestCase(unittest.TestCase):
    """A Stack TestCase"""

    def test_to_create_stack(self):
        stack = core.Stack('StackTesting')
        assert stack.name == 'StackTesting'

    def test_to_push_object_to_the_stack(self):
        stack = core.Stack('StackTesting')
        # Make a fake Nagios Object
        obj = type('foo', (object,), dict(type='host', pk='bar', name='baz'))
        stack.push(obj)
        assert 'host' in stack.objects
        assert obj == stack.objects['host']['bar']

    def test_to_raise_DuplicateError_if_pk_already_exist(self):
        stack = core.Stack('StackTesting')
        # Make a fake Nagios Object
        obj = type('foo', (object,), dict(type='host', pk='bar', name='baz'))
        stack.push(obj)
        with self.assertRaises(exceptions.DuplicateError):
            #  Make a new Object with a same type and pk
            obj = type('Fo', (object,), dict(type='host', pk='bar', name='BA'))
            stack.push(obj)
