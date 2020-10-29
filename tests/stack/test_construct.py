# Unit tests for Construct

import unittest
from collections.abc import Iterable

from ndk.construct import Construct
from ndk.stack import Stack


class ConstructTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack('ConstructTesting')

    def test_construct(self):
        const = Construct(self.stack)
        assert const.stack is self.stack
        assert const.stack.name == 'ConstructTesting'

        const2 = Construct('new stack')
        assert const2.stack is not self.stack
        assert const2.stack.name == 'new stack'

    def test_object_type(self):
        assert Construct.__object_type__
        assert Construct.__object_type__ == 'template'

    def test_pk(self):
        const = Construct(self.stack)
        assert const.pk == 'template'

    def test_prxfix(self):
        const = Construct(self.stack)
        assert const.prefix == 'define template {'

    def test_suffix(self):
        const = Construct(self.stack)
        assert const.suffix == '}'

    def test_iter(self):
        const = Construct(self.stack)
        assert isinstance(const.__iter__(), Iterable)
        assert isinstance(const, Iterable)

    def test_synth(self):
        const = Construct(self.stack)
        tmp = ('define template {', '}')
        assert '\n'.join(tmp) == const.synth()
