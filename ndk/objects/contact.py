from enum import Enum

from ndk import core, fields


class ChoiceMixin:

    @classmethod
    def choices(cls):
        for name, member in cls.__members__.items():
            if not name == 'NO':
                yield member

    @classmethod
    def all(cls):
        items = (member.value for member in cls.choices())
        return list(items)

    @classmethod
    def empty(cls):
        return cls.NO


class HostNotifications(ChoiceMixin, Enum):
    """
    This directive is used to define the host states for
    which notifications can be sent out to this contact.

    Valid options:
        - d = notify on DOWN host states
        - u = notify on UNREACHABLE host states
        - r = notify on host recoveries (UP states)
        - f = notify when the host starts and stops flapping
        - s = notify when host scheduled downtime starts and ends
        - n = the contact will not receive any type of host notifications
    """

    DOWN = 'd'
    UNREACHABLE = 'u'
    RECOVERY = 'r'
    FLAPPING = 'f'
    SCHEDULED = 's'
    NO = 'n'


class ServiceNotifications(ChoiceMixin, Enum):
    """
    This directive is used to define the service states for
    which notifications can be sent out to this contact.

    Valid options:
        - w = notify on WARNING service states
        - u = notify on UNKNOWN service states
        - c = notify on CRITICAL service states
        - r = notify on service recoveries (OK states)
        - f = notify when the service starts and stops flapping
        - n = the contact will not receive any type of service notifications.
    """

    WARNING = 'w'
    UNKNOWN = 'u'
    CRITICAL = 'c'
    RECOVERY = 'r'
    FLAPPING = 'f'
    SCHEDULED = 's'
    NO = 'n'


class ContactConstruct(core.Object):
    """
    L1 Construct: Nagios::Object::Contact

    This construct correspond directly to object defined by Nagios.
    """

    class Meta:
        object_type = 'contact'

    contact_name = fields.StringField(primary_key=True, required=True)
    alias = fields.StringField()
    contactgroups = fields.ForeignKey(relation='ContactGroup')
    minimum_importance = fields.IntegerField()
    host_notifications_enabled = fields.BooleanField(required=True)
    service_notifications_enabled = fields.BooleanField(required=True)
    host_notifications_period = fields.ForeignKey(
        relation='TimePeriod', required=True)
    service_notifications_period = fields.ForeignKey(
        relation='TimePeriod', required=True)
    host_notifications_options = fields.ChoiceField(
        choices=HostNotifications, required=True)
    service_notifications_options = fields.ChoiceField(
        choices=ServiceNotifications, required=True)
    host_notification_commands = fields.ForeignKey(
        relation='Command', required=True)
    service_notification_commands = fields.ForeignKey(
        relation='Command', required=True)
    email = fields.StringField()
    pager = fields.StringField()
    addressx = fields.StringField()
    can_submit_commands = fields.BooleanField()
    retain_status_information = fields.BooleanField()
    retain_nonstatus_information = fields.BooleanField()

    def __init__(
            self, stack, contact_name, host_notifications_enabled,
            service_notifications_enabled, host_notifications_period,
            service_notifications_period, host_notifications_options,
            service_notifications_options, host_notification_commands,
            service_notification_commands, alias=None, contactgroups=None,
            minimum_importance=None, email=None, pager=None, addressx=None,
            can_submit_commands=None, retain_status_information=None,
            retain_nonstatus_information=None):
        super().__init__(
            stack, contact_name=contact_name,
            host_notifications_enabled=host_notifications_enabled,
            service_notifications_enabled=service_notifications_enabled,
            host_notifications_period=host_notifications_period,
            service_notifications_period=service_notifications_period,
            host_notifications_options=host_notifications_options,
            service_notifications_options=service_notifications_options,
            host_notification_commands=host_notification_commands,
            service_notification_commands=service_notification_commands,
            alias=alias, contactgroups=contactgroups,
            minimum_importance=minimum_importance, email=email, pager=pager,
            addressx=addressx, can_submit_commands=can_submit_commands,
            retain_status_information=retain_status_information,
            retain_nonstatus_information=retain_nonstatus_information)


class Contact(ContactConstruct):
    """
    L2 Construct: Nagios::Object::Contact

    L2 encapsulate L1 modules, it is developed to address specific use
    cases and sensible defaults.
    """

    def __init__(
            self, stack, contact_name, host_notifications_period,
            service_notifications_period, host_notification_commands,
            service_notification_commands, host_notifications_enabled=True,
            service_notifications_enabled=True,
            host_notifications_options=HostNotifications.all(),
            service_notifications_options=ServiceNotifications.all(),
            **kwargs):
        super().__init__(
            stack=stack, contact_name=contact_name,
            host_notifications_period=host_notifications_period,
            service_notifications_period=service_notifications_period,
            host_notification_commands=host_notification_commands,
            service_notification_commands=service_notification_commands,
            host_notifications_enabled=host_notifications_enabled,
            service_notifications_enabled=service_notifications_enabled,
            host_notifications_options=host_notifications_options,
            service_notifications_options=service_notifications_options,
            **kwargs)


class Email(Contact):
    """
    L3 Construct: Nagios::Object::Contact

    L3 declare a resource to create particular use cases.
    """

    def __init__(
            self, stack, contact_name, email, host_notifications_period,
            service_notifications_period, host_notification_commands,
            service_notification_commands, **kwargs):
        super().__init__(
            stack, contact_name=contact_name, email=email,
            host_notifications_period=host_notifications_period,
            service_notifications_period=service_notifications_period,
            host_notification_commands=host_notification_commands,
            service_notification_commands=service_notification_commands,
            **kwargs)
