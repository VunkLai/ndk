from enum import Enum

from ndk import fields, core


class InitialState(Enum):
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


class FlapDetection(Enum):
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


class Notification(Enum):
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


class Stalking(Enum):
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


class NgsHost(core.Object):
    """
    L1 Construct: Nagios::Object::Host
    """

    class Meta:
        object_type = 'host'

    host_name = fields.StringField(primary_key=True, requried=True)
    alias = fields.StringField(requried=True)
    display_name = fields.StringField()
    address = fields.Ipv4Field()
    parents = fields.ForeignKey('Host')
    importance = fields.IntegerField()
    hostgroups = fields.ForeignKey('HostGroup')
    check_command = fields.ForeignKey('Command')
    initial_state = fields.ChoiceField(choices=InitialState)
    max_check_attempts = fields.IntegerField(requried=True)
    check_interval = fields.IntegerField()
    retry_interval = fields.IntegerField()
    active_checks_enabled = fields.BooleanField()
    passive_checks_enabled = fields.BooleanField()
    check_period = fields.ForeignKey('TimePeriod', requried=True)
    obsess_over_host = fields.BooleanField()
    check_freshness = fields.BooleanField()
    freshness_threshold = fields.IntegerField()
    event_handler = fields.ForeignKey('Command')
    event_handler_enabled = fields.BooleanField()
    low_flap_threshold = fields.IntegerField()
    high_flap_threshold = fields.IntegerField()
    flap_detection_enabled = fields.BooleanField()
    flap_detection_options = fields.ChoiceField(choices=FlapDetection)
    process_perf_data = fields.BooleanField()
    retain_status_information = fields.BooleanField()
    retain_nonstatus_information = fields.BooleanField()
    contacts = fields.ForeignKey('Contact', composite_key=True)
    contact_groups = fields.ForeignKey('ContactGroup', composite_key=True)
    notification_interval = fields.IntegerField(requried=True)
    first_notification_delay = fields.IntegerField()
    notification_period = fields.ForeignKey('TimePeriod', requried=True)
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
    # _2d_coords = fields.ChoiceField(choices=HostOptions, requried=False)
    # _3d_coords = fields.ChoiceField(choices=HostOptions, requried=False)


class Host(NgsHost):
    """
    L2 Construct: Nagios::Object::Host
    """

    def __init__(self, stack, host_name=None, alias=None, display_name=None,
                 address=None, parents=None, importance=None,
                 hostgroups=None, check_command=None, initial_state=None,
                 max_check_attempts=None, check_interval=None,
                 retry_interval=None, active_checks_enabled=None,
                 passive_checks_enabled=None, check_period=None,
                 obsess_over_host=None, check_freshness=None,
                 freshness_threshold=None, event_handler=None,
                 event_handler_enabled=None, low_flap_threshold=None,
                 high_flap_threshold=None, flap_detection_enabled=None,
                 flap_detection_options=None, process_perf_data=None,
                 retain_status_information=None,
                 retain_nonstatus_information=None,
                 contacts=None, contact_groups=None,
                 notification_interval=None, first_notification_delay=None,
                 notification_period=None, notification_options=None,
                 notifications_enabled=None, stalking_options=None,
                 notes=None, notes_url=None, action_url=None,
                 icon_image=None, icon_image_alt=None, vrml_image=None,
                 statusmap_image=None,
                 # _2d_coords=None, # _3d_coords=None
                 ):

        super().__init__(stack, host_name=host_name, alias=alias,
                         display_name=display_name, address=address,
                         parents=parents, importance=importance,
                         hostgroups=hostgroups, check_command=check_command,
                         initial_state=initial_state,
                         max_check_attempts=max_check_attempts,
                         check_interval=check_interval,
                         retry_interval=retry_interval,
                         active_checks_enabled=active_checks_enabled,
                         passive_checks_enabled=passive_checks_enabled,
                         check_period=check_period,
                         obsess_over_host=obsess_over_host,
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
                         contacts=contacts, contact_groups=contact_groups,
                         notification_interval=notification_interval,
                         first_notification_delay=first_notification_delay,
                         notification_period=notification_period,
                         notification_options=notification_options,
                         notifications_enabled=notifications_enabled,
                         stalking_options=stalking_options, notes=notes,
                         notes_url=notes_url, action_url=action_url,
                         icon_image=icon_image,
                         icon_image_alt=icon_image_alt,
                         vrml_image=vrml_image,
                         statusmap_image=statusmap_image,
                         # _2d_coords=_2d_coords, _3d_coords=_3d_coords,
                         )
