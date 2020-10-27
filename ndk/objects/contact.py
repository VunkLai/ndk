
import attr
from ndk.definitions import contact
from ndk.options import contact as options


@attr.s
class Contact(contact.ContactDirective):
    host_notifications_enabled = attr.ib(default=True)
    service_notifications_enabled = attr.ib(default=True)
    host_notifications_options = attr.ib(
        default=options.HostNotifications.all())
    service_notifications_options = attr.ib(
        default=options.ServiceNotifications.all())


@attr.s
class Email(Contact):
    # set email required
    email = attr.ib(type=str, converter=str, kw_only=True)
