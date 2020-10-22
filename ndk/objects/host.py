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


class InitialState(ChoiceMixin, Enum):
    """
    Override the initial state for a Host

    By default Nagios will assume that all hosts are in UP states when it starts.
    You can override the initial state for a host by using this directive.

    Valid options:
        - o = UP
        - d = DOWN
        - u = UNREACHABLE
    """

    UP = 'o'
    DOWN = 'd'
    UNREACHABLE = 'u'


class FlapDetection(ChoiceMixin, Enum):
    """
    This directive is used to determine what host states the flap detection logic will use for this host.

    Valid options:
        - o = UP
        - d = DOWN
        - u = UNREACHABLE
    """

    UP = 'o'
    DOWN = 'd'
    UNREACHABLE = 'u'


class Notification(ChoiceMixin, Enum):
    """
    This directive is used to determine when notifications for the host should be sent out.

    If you do not specify any notification options, Nagios will assume that you want notifications to be sent out for all possible states.

    Valid options:
        - d = send notifications on a DOWN state
        - u = send notifications on an UNREACHABLE state
        - r = send notifications on recoveries (OK state)
        - f = send notifications when the host starts and stops flapping
        - s = send notifications when scheduled downtime starts and ends
        - n = no host notifications will be sent out
    """

    DOWN = 'd'
    UNREACHABLE = 'u'
    RECOVERY = 'r'
    FLAPPING = 'f'
    SCHEDULED = 's'
    NO = 'n'


class Stalking(ChoiceMixin, Enum):
    """
    This directive determines which host states "stalking" is enabled for.

    Note: As of Core 4.4.0 you can use the N option to log event states when notifications are sent out.

    Valid options:
        - o = stalk on UP states
        - d = stalk on DOWN states
        - u = stalk on UNREACHABLE states
    """

    UP = 'o'
    DOWN = 'd'
    UNREACHABLE = 'u'


class HostConstruct(core.Object):
    """
    L1 Construct: Nagios::Object::Host
    """

    class Meta:
        object_type = 'host'

    host_name = fields.StringField(primary_key=True, required=True)
    alias = fields.StringField(required=True)
    display_name = fields.StringField()
    address = fields.Ipv4Field()
    parents = fields.ForeignKey(relation='Host')
    importance = fields.IntegerField()
    hostgroups = fields.ForeignKey(relation='HostGroup')
    check_command = fields.ForeignKey(relation='Command')
    initial_state = fields.ChoiceField(choices=InitialState)
    max_check_attempts = fields.IntegerField(required=True)
    check_interval = fields.IntegerField()
    retry_interval = fields.IntegerField()
    active_checks_enabled = fields.BooleanField()
    passive_checks_enabled = fields.BooleanField()
    check_period = fields.ForeignKey(relation='TimePeriod', required=True)
    obsess_over_host = fields.BooleanField()
    check_freshness = fields.BooleanField()
    freshness_threshold = fields.IntegerField()
    event_handler = fields.ForeignKey(relation='Command')
    event_handler_enabled = fields.BooleanField()
    low_flap_threshold = fields.IntegerField()
    high_flap_threshold = fields.IntegerField()
    flap_detection_enabled = fields.BooleanField()
    flap_detection_options = fields.ChoiceField(choices=FlapDetection)
    process_perf_data = fields.BooleanField()
    retain_status_information = fields.BooleanField()
    retain_nonstatus_information = fields.BooleanField()
    contacts = fields.ForeignKey(relation='Contact', composite_key=True)
    contact_groups = fields.ForeignKey(
        relation='ContactGroup', composite_key=True)
    notification_interval = fields.IntegerField(required=True)
    first_notification_delay = fields.IntegerField()
    notification_period = fields.ForeignKey(
        relation='TimePeriod', required=True)
    notification_options = fields.ChoiceField(choices=Notification)
    notifications_enabled = fields.BooleanField()
    stalking_options = fields.ChoiceField(choices=Stalking)
    notes = fields.StringField()
    notes_url = fields.StringField()
    action_url = fields.StringField()
    icon_image = fields.StringField()
    icon_image_alt = fields.StringField()
    vrml_image = fields.StringField()
    statusmap_image = fields.StringField()
    _2d_coords = fields.StringField()
    _3d_coords = fields.StringField()

    def __init__(
            self, stack, host_name, alias, max_check_attempts, check_period,
            notification_interval, notification_period, display_name=None,
            address=None, parents=None, importance=None, hostgroups=None,
            check_command=None, initial_state=None, check_interval=None,
            retry_interval=None, active_checks_enabled=None,
            passive_checks_enabled=None, obsess_over_host=None,
            check_freshness=None, freshness_threshold=None, event_handler=None,
            event_handler_enabled=None, low_flap_threshold=None,
            high_flap_threshold=None, flap_detection_enabled=None,
            flap_detection_options=None, process_perf_data=None,
            retain_status_information=None, retain_nonstatus_information=None,
            contacts=None, contact_groups=None, first_notification_delay=None,
            notification_options=None, notifications_enabled=None,
            stalking_options=None, notes=None, notes_url=None, action_url=None,
            icon_image=None, icon_image_alt=None, vrml_image=None,
            statusmap_image=None, _2d_coords=None, _3d_coords=None):

        super().__init__(
            stack, host_name=host_name, alias=alias,
            max_check_attempts=max_check_attempts, check_period=check_period,
            notification_interval=notification_interval,
            notification_period=notification_period, display_name=display_name,
            address=address, parents=parents, importance=importance,
            hostgroups=hostgroups, check_command=check_command,
            initial_state=initial_state, check_interval=check_interval,
            retry_interval=retry_interval,
            active_checks_enabled=active_checks_enabled,
            passive_checks_enabled=passive_checks_enabled,
            obsess_over_host=obsess_over_host, check_freshness=check_freshness,
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
            contacts=contacts, contact_groups=contact_groups,
            first_notification_delay=first_notification_delay,
            notification_options=notification_options,
            notifications_enabled=notifications_enabled,
            stalking_options=stalking_options, notes=notes,
            notes_url=notes_url, action_url=action_url, icon_image=icon_image,
            icon_image_alt=icon_image_alt, vrml_image=vrml_image,
            statusmap_image=statusmap_image, _2d_coords=_2d_coords,
            _3d_coords=_3d_coords)


class Host(HostConstruct):
    """
    L2 Construct: Nagios::Object::Host
    """

    def __init__(
            self, stack, host_name, address, notification_period,
            check_command, max_check_attempts=5, check_period=3,
            notification_interval=60, alias=None, check_interval=None,
            retry_interval=None, active_checks_enabled=True,
            passive_checks_enabled=False, event_handler=None,
            event_handler_enabled=False, flap_detection_enabled=True,
            flap_detection_options=None, contacts=None, contact_groups=None,
            first_notification_delay=None, notifications_enabled=True,
            notification_options=Notification.all(),
            **kwargs):
        alias = alias or host_name
        super().__init__(
            stack, host_name=host_name, alias=alias, address=address,
            max_check_attempts=max_check_attempts, check_period=check_period,
            notification_interval=notification_interval,
            notification_period=notification_period,
            check_command=check_command,
            check_interval=check_interval,
            retry_interval=retry_interval,
            active_checks_enabled=active_checks_enabled,
            passive_checks_enabled=passive_checks_enabled,
            event_handler=event_handler,
            event_handler_enabled=event_handler_enabled,
            flap_detection_enabled=flap_detection_enabled,
            flap_detection_options=flap_detection_options,
            contacts=contacts, contact_groups=contact_groups,
            first_notification_delay=first_notification_delay,
            notification_options=notification_options,
            notifications_enabled=notifications_enabled, **kwargs)
