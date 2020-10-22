from ndk import core, fields


class CommandConstruct(core.Object):
    """
    L1 Construct: Nagios::Object::Command

    This construct correspond directly to Command defined by Nagios.
    """

    class Meta:
        object_type = 'command'

    command_name = fields.StringField(primary_key=True, required=True)
    command_line = fields.StringField(required=True)

    def __init__(self, stack, command_name, command_line):
        super().__init__(stack,
                         command_name=command_name,
                         command_line=command_line)


class Command(CommandConstruct):
    """
    L2 Construct: Nagios::Object::Command

    Command encapsulate L1 modules, it is developed to address specific use 
    cases and sensible defaults.
    """

    def __init__(self, stack, **kwargs):
        # All fields are requred in the construct
        super().__init__(stack, **kwargs)


class Ping(Command):
    """
    L3 Construct: Nagios::Object::Command

    L3 declare a resource to create particular use cases.
    """

    def __init__(self, stack, command_name=None):
        name = command_name or 'check-host-alive'
        cmd = '$USER1$/check_ping -H $HOSTADDRESS$ -w 30.0,80% -c 50.0,100%'
        super().__init__(stack, command_name=name, command_line=cmd)
