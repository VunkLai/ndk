# Nagios Development Kit

NDK is a software development framework for defining Nagios Object in code and deploy it to your Nagios.

Use the NDK to define your resources you want monitor to.

## Quick Start

### Example

```python
from ndk.stack import Stack

from ndk.objects.command import Email
from ndk.objects.host import Host
from ndk.objects.timeperiod import TwentyFourSeven

stack = Stack('StackTesting')
_24x7 = TwentyFourSeven(stack)
email = Email(stack)
host = Host(stack, host_name='foo',
            check_period=self.tp, notification_period=self.tp)

print(stack.synth())
```

### Testing

```
pytest
```
