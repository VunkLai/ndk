

import attr
from ndk.construct import Construct
from ndk.directives import *
from ndk.options import contact as options


@attr.s
class ContactDirective(Construct):
    __object_type__ = 'contact'

    contact_name = PrimaryKey()
    alias = StringField()
    contactgroups = OneToMany('ContactGroup')
    minimum_importance = IntegerField()
    host_notifications_enabled = BooleanField(required=True)
    service_notifications_enabled = BooleanField(required=True)
    host_notifications_period = OneToOne(
        'TimePeriod', required=True)
    service_notifications_period = OneToOne(
        'TimePeriod', required=True)
    host_notifications_options = ChoiceField(
        options.HostNotifications, required=True)
    service_notifications_options = ChoiceField(
        options.ServiceNotifications, required=True)
    host_notification_commands = OneToOne('Command', required=True)
    service_notification_commands = OneToOne('Command', required=True)
    email = StringField()
    pager = StringField()
    addressx = StringField()
    can_submit_commands = BooleanField()
    retain_status_information = BooleanField()
    retain_nonstatus_information = BooleanField()

    @property
    def pk(self):
        return self.contact_name
