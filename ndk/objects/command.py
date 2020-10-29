import attr
from ndk.definitions import command


@attr.s
class Command(command.CommandDirective):
    pass


@attr.s(frozen=True)
class Ping(Command):
    command_name = attr.ib(default='ping')
    command_line = attr.ib(
        default='$USER1$/check_ping -H $HOSTADDRESS$ -w 30.0,80% -c 50.0,100%')


@attr.s(frozen=True)
class Email(Command):
    command_name = attr.ib(default='send-by-email')
    command_line = attr.ib(default='smtp')
