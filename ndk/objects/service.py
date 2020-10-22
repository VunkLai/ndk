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
        return list(cls.choices())

    @classmethod
    def empty(cls):
        return cls.NO


class InitialState(ChoiceMixin, Enum):
    """
    Override the initial state for a Host

    By default Nagios will assume that all services are in OK states when it starts.
    You can override the initial state for a host by using this directive.

    Valid options:
      - o = OK
      - w = WARNING
      - u = UNKNOWN
      - c = CRITICAL
    """

    OK = 'o'
    WARNING = 'w'
    UNKNOWN = 'u'
    CRITICAL = 'c'


class FlapDetection(ChoiceMixin, Enum):
    """
    This directive is used to determine what service states the flap detection
    logic will use for this service.

    Valid options:
      - o = OK
      - w = WARNING
      - u = UNKNOWN
      - c = CRITICAL
    """

    OK = 'o'
    WARNING = 'w'
    UNKNOWN = 'u'
    CRITICAL = 'c'


class Notification(ChoiceMixin, Enum):
    """
    This directive is used to determine
    when notifications for the service should be sent out.

    If you do not specify any notification options,
    Nagios will assume that you want notifications to be sent out
    for all possible states.

    Valid options:
      - w = send notifications on a WARNING state
      - c = send notifications on a CRITICAL state
      - u = send notifications on an UNKNOWN state
      - r = send notifications on recoveries (OK state)
      - f = send notifications when the service starts and stops flapping
      - s = send notifications when scheduled downtime starts and ends
      - n = no service notifications will be sent out
    """

    WARNING = 'w'
    CRITICAL = 'c'
    UNKNOWN = 'u'
    RECOVERY = 'r'
    FLAPPING = 'f'
    SCHEDULED = 's'
    NO = 'n'


class Stalking(ChoiceMixin, Enum):
    """
    This directive determines which service states "stalking" is enabled for.

    Note: As of Core 4.4.0 you can use the N option to log event states when notifications are sent out.

    Valid options:
      - o = stalk on OK states
      - w = stalk on WARNING states
      - u = stalk on UNKNOWN states
      - c = stalk on CRITICAL states
    """

    OK = 'o'
    WARNING = 'w'
    UNKNOWN = 'u'
    CRITICAL = 'c'


class ServiceConstruct(core.Object):
    """
    L1 Construct: Nagios::Object::Service
    """

    class Meta:
        object_type = 'service'

    host_name = fields.StringField(primary_key=True, required=True)
    hostgroup_name = fields.ForeignKey(relation='HostGroup')
    service_description = fields.StringField(primary_key=True, required=True)
    display_name = fields.StringField()
    parents = fields.ForeignKey(relation='Service')
    importance = fields.IntegerField()
    servicegroups = fields.ForeignKey(relation='ServiceGroup')
    is_volatile = fields.BooleanField()
    check_command = fields.StringField(required=True)
    initial_state = fields.ChoiceField(choices=InitialState)
    max_check_attempts = fields.IntegerField(required=True)
    check_interval = fields.IntegerField(required=True)
    retry_interval = fields.IntegerField(required=True)
    active_checks_enabled = fields.BooleanField()
    passive_checks_enabled = fields.BooleanField()
    check_period = fields.ForeignKey(relation='TimePeriod', required=True)
    obsess_over_service = fields.BooleanField()
    check_freshness = fields.BooleanField()
    freshness_threshold = fields.IntegerField()
    event_handler = fields.ForeignKey(relation='Command')
    event_handler_enabled = fields.BooleanField()
    low_flap_threshold = fields.IntegerField()
    high_flap_threshold = fields.IntegerField()
    flap_detection_enabled = fields.BooleanField()
    flap_detection_options = fields.ChoiceField(
        choices=FlapDetection)
    process_perf_data = fields.BooleanField()
    retain_status_information = fields.BooleanField()
    retain_nonstatus_information = fields.BooleanField()
    notification_interval = fields.IntegerField(required=True)
    first_notification_delay = fields.IntegerField()
    notification_period = fields.ForeignKey(
        relation='TimePeriod', required=True)
    notification_options = fields.ChoiceField(
        choices=Notification)
    notifications_enabled = fields.BooleanField()
    contacts = fields.ForeignKey(relation='Contact', composite_key=True)
    contact_groups = fields.ForeignKey(
        relation='ContactGroup', composite_key=True)
    stalking_options = fields.ChoiceField(choices=Stalking)
    notes = fields.StringField()
    notes_url = fields.StringField()
    action_url = fields.StringField()
    icon_image = fields.StringField()
    icon_image_alt = fields.StringField()

    def __init__(
            self, stack, host_name, service_description, check_command,
            check_interval, retry_interval, check_period,
            notification_interval, notification_period, hostgroup_name=None,
            display_name=None, parents=None, importance=None,
            servicegroups=None, is_volatile=None, initial_state=None,
            max_check_attempts=None, active_checks_enabled=None,
            passive_checks_enabled=None, obsess_over_service=None,
            check_freshness=None, freshness_threshold=None, event_handler=None,
            event_handler_enabled=None, low_flap_threshold=None,
            high_flap_threshold=None, flap_detection_enabled=None,
            flap_detection_options=None, process_perf_data=None,
            retain_status_information=None, retain_nonstatus_information=None,
            first_notification_delay=None, notification_options=None,
            notifications_enabled=None, contacts=None, contact_groups=None,
            stalking_options=None, notes=None, notes_url=None, action_url=None,
            icon_image=None, icon_image_alt=None):
        super().__init__(
            stack, host_name=host_name, hostgroup_name=hostgroup_name,
            service_description=service_description, display_name=display_name,
            parents=parents, importance=importance,
            servicegroups=servicegroups, is_volatile=is_volatile,
            check_command=check_command, initial_state=initial_state,
            max_check_attempts=max_check_attempts,
            check_interval=check_interval, retry_interval=retry_interval,
            active_checks_enabled=active_checks_enabled,
            passive_checks_enabled=passive_checks_enabled,
            check_period=check_period, obsess_over_service=obsess_over_service,
            check_freshness=check_freshness,
            freshness_threshold=freshness_threshold,
            event_handler=event_handler,
            event_handler_enabled=event_handler_enabled,
            low_flap_threshold=low_flap_threshold,
            high_flap_threshold=high_flap_threshold,
            flap_detection_enabled=flap_detection_enabled,
            flap_detection_options=flap_detection_options,
            process_perf_data=process_perf_data,
            retain_status_information=retain_status_information,
            retain_nonstatus_information=retain_nonstatus_information,
            notification_interval=notification_interval,
            first_notification_delay=first_notification_delay,
            notification_period=notification_period,
            notification_options=notification_options,
            notifications_enabled=notifications_enabled, contacts=contacts,
            contact_groups=contact_groups, stalking_options=stalking_options,
            notes=notes, notes_url=notes_url, action_url=action_url,
            icon_image=icon_image, icon_image_alt=icon_image_alt)


class Service(ServiceConstruct):
    """
    L2 Construct: Nagios::Object::Service
    """

    def __init__(
            self, stack, host_name, service_description, check_command,
            notification_period, check_interval=3, retry_interval=2,
            check_period=5, notification_interval=60, max_check_attempts=5,
            active_checks_enabled=True, passive_checks_enabled=False,
            event_handler=None, event_handler_enabled=False,
            flap_detection_enabled=True, flap_detection_options=None,
            first_notification_delay=None, notification_options=None,
            notifications_enabled=True, contacts=None, contact_groups=None, **
            kwargs):
        super().__init__(
            stack, host_name=host_name,
            service_description=service_description,
            check_command=check_command, max_check_attempts=max_check_attempts,
            check_interval=check_interval, retry_interval=retry_interval,
            active_checks_enabled=active_checks_enabled,
            passive_checks_enabled=passive_checks_enabled,
            check_period=check_period, event_handler=event_handler,
            event_handler_enabled=event_handler_enabled,
            flap_detection_enabled=flap_detection_enabled,
            flap_detection_options=flap_detection_options,
            notification_interval=notification_interval,
            first_notification_delay=first_notification_delay,
            notification_period=notification_period,
            notification_options=notification_options,
            notifications_enabled=notifications_enabled, contacts=contacts,
            contact_groups=contact_groups, **kwargs)
