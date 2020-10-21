from ndk import core, fields


class Host(core.Object):
    class Meta:
        object_type = 'host'

    host_name = fields.StringField(primary_key=True)

