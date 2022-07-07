import mongoengine as me
from mongoengine_mate import ExtendedDocument


class BlockedTokenModel(ExtendedDocument):
    jti = me.StringField()
    created_at = me.DateTimeField()

    meta = {
        'strict': False,
    }
