from ndk import core, objects
from ndk.objects import host


class Infrastructure:

    def __init__(self, stack):
        _24x7 = objects.TwentyFourSeven(stack)
        objects.Host(stack, host_name='Infra', address='127.0.0.1',
                     check_command=objects.command.Ping(stack),
                     notification_period=_24x7,
                     check_period=_24x7)


stack = core.Stack('StackExample')
Infrastructure(stack)

print(stack.synth())
