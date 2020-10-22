import unittest

# from . import models
from ndk import core, exceptions, fields, objects


class NagiosTestCase(unittest.TestCase):

    def test_raise_IntegrityError_when_create_new_class(self):
        with self.assertRaises(exceptions.IntegrityError):
            class EmptyObject(core.Object):
                pass

        with self.assertRaises(exceptions.IntegrityError):
            class ObjectWithoutPK(core.Object):
                class Meta:
                    object_type = 'host'

                directive = fields.Field()

        with self.assertRaises(exceptions.IntegrityError):
            class ObjectWithoutObjectType(core.Object):

                directive = fields.Field(primary_key=True)

    def test_to_create_new_class(self):
        class GoodObject(core.Object):
            class Meta:
                object_type = 'host'
            host_name = fields.Field(primary_key=True)

        assert 'host' == GoodObject.__object_type__
        assert 'host_name' in GoodObject.__mappings__
        assert 'host_name' in GoodObject.__primary_key__
        assert not GoodObject.__composite_key__
        stack = core.Stack('ObjectTesting')
        host = GoodObject(stack, host_name='foo')

    def test_if_pk_has_certain_format(self):
        class ObjectWithOenPK(core.Object):
            class Meta:
                object_type = 'foo'
            host_name = fields.StringField(primary_key=True)

        class ObjectWithTwoPKs(core.Object):
            class Meta:
                object_type = 'foo'
            host_name = fields.StringField(primary_key=True)
            alias = fields.StringField(primary_key=True)

        stack = core.Stack('ObjectTesting')
        host = ObjectWithOenPK(stack, host_name='Foo Bar')
        assert host.pk == 'foo-bar'

        host = ObjectWithTwoPKs(stack, host_name='Foo Bar', alias='BAZ')
        assert host.pk == 'foo-bar::baz'

    def test_required_is_works_in_object(self):
        class Host(core.Object):
            class Meta:
                object_type = 'asdf'

            host_name = fields.StringField(required=True, primary_key=True)
            address = fields.Ipv4Field(required=True)

        stack = core.Stack('FieldTesting')
        with self.assertRaises(exceptions.IntegrityError):
            host = Host(stack, host_name='foo')
            host.is_valid()

        host = Host(stack, host_name='bar', address='127.0.0.1')
        host.is_valid()

    def test_synth_is_works(self):
        stack = core.Stack('ObjectTesting')
        _7x24 = objects.TwentyFourSeven(stack, 'tp-24x7')
        cmd = objects.command.Ping(stack)
        host = objects.Host(
            stack, host_name='foo', address='127.0.0.1',
            check_period=_7x24,
            notification_period=_7x24,
            check_command=cmd)

        define = '\n'.join((
            'define command {',
            '    command_name    check-host-alive',
            '    command_line    $USER1$/check_ping -H $HOSTADDRESS$ -w 30.0,80% -c 50.0,100%',
            '}'
        ))
        assert define == cmd.synth()
        assert 'check_period    tp-24x7' in host.synth()
        assert 'notification_options    d,u,r,f,s' in host.synth()
        assert define in stack.synth()
