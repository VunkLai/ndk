from ndk import fields, core


class CommandConstruct(core.Object):
    """
    L1 Construct: Nagios::Object::Command
    """

    class Meta:
        object_type = 'command'

    command_name = fields.StringField(primary_key=True, required=True)
    command_line = fields.StringField(required=True)

    def __init__(self, stack, command_name, command_line):
        super().__init__(stack, command_name, command_line)


class Command(CommandConstruct):
    """
    L2 Construct: Nagios::Object::Command
    """

    def __init__(self, stack, **kwargs):
        super().__init__(stack, **kwargs)

    @staticmethod
    def ping(stack):
        return Ping(stack)


class Ping(Command):
    """
    L3 Construct: Nagios::Object::Command
    """

    command_name = fields.StringField(
        primary_key=True, required=True, default='check-host-alive')
    command_line = fields.StringField(
        required=True, default='$USER1$/check_ping -H $HOSTADDRESS$ -w 30.0,80% -c 50.0,100%')
