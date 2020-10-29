# Unit tests for Stack

import unittest
from collections import defaultdict
from collections.abc import Iterable

from ndk.construct import Construct
from ndk.stack import Stack


class StackTestCase(unittest.TestCase):

    def test_name(self):
        with self.assertRaises(TypeError):
            # `.name` is requried to initialize Stack
            Stack()
        stack = Stack('StackTesting')
        assert stack.name == 'StackTesting'

    def test_objects(self):
        stack = Stack('StackTesting')
        assert isinstance(stack.objects, defaultdict)

    def test_iter(self):
        stack = Stack('StackTesting')
        assert isinstance(stack.__iter__(), Iterable)
        assert isinstance(stack, Iterable)
        Construct(stack)
        assert len(list(stack)) == 1

    def test_singleton(self):
        # for .converter
        stack = Stack.singleton('StackTesting')
        new_stack = Stack.singleton(stack)
        assert stack is new_stack

    def test_push(self):
        stack = Stack('StackTesting')

        obj = type('foo', (object,), dict(__object_type__='foo', bar='baz'))
        with self.assertRaises(AssertionError):
            stack.push(obj)

        obj = Construct(stack)
        stack.push(obj)
        assert 'template' in stack.objects
        assert len(stack.objects['template']) == 1

    def test_synth(self):
        stack = Stack('StackTesting')
        Construct(stack)
        tmp = (
            'define template {',
            '}'
        )
        print(stack.synth())
        assert '\n'.join(tmp) == stack.synth()
