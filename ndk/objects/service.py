import attr
from ndk.definitions import service
from ndk.options import service as options


@attr.s
class Service(service.ServiceDirective):

    check_interval=attr.ib(default=3)
    retry_interval=attr.ib(default=2)
    check_period=attr.ib(default=5)
    notification_interval=attr.ib(default=60)
    max_check_attempts=attr.ib(default=5)
    active_checks_enabled=attr.ib(default=True)
    passive_checks_enabled=attr.ib(default=False)
    event_handler_enabled=attr.ib(default=False)
    flap_detection_enabled=attr.ib(default=True)
    notifications_enabled=attr.ib(default=True)
