import mongoengine as me
from mongoengine_mate import ExtendedDocument

class UserModel(ExtendedDocument):
    name = me.StringField()
    location = me.StringField()
    # email = me.StringField()
    # password = me.StringField()

    meta = {
        'strict': False,
    }
