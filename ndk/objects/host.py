import attr
from ndk.definitions import host
from ndk.options import host as options


@attr.s
class Host(host.HostDirective):
    max_check_attempts = attr.ib(default=5)
    notification_interval = attr.ib(default=60)
    active_checks_enabled = attr.ib(default=True)
    passive_checks_enabled = attr.ib(default=False)
    event_handler_enabled = attr.ib(default=False)
    flap_detection_enabled = attr.ib(default=True)
    notifications_enabled = attr.ib(default=True)
    notification_options = options.Notification.all()
    alias = attr.ib(type=str,
                    converter=str,
                    validator=attr.validators.instance_of(str),
                    kw_only=True)

    @alias.default
    def _set_alias_as_host_name(self):
        return self.host_name
