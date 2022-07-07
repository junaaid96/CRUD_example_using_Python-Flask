from unicodedata import name
from db_models.user_model import UserModel

class RootService:

    @staticmethod
    def create(data):
        UserModel.col().insert_one(data)

    @staticmethod
    def get_all():
        return list(UserModel.col().find({ }))

    @staticmethod
    def get_one(data):
        return UserModel.col().find_one(data)

    @staticmethod
    def update(query, body):
        UserModel.col().update_one(query, {"$set": body})

    @staticmethod
    def delete_one(query):
        UserModel.col().delete_one(query)

    @staticmethod
    def delete_all():
        UserModel.col().drop()