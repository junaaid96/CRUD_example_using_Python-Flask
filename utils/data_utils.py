import json

from db_models.user_model import UserModel


class DataUtils:

    @staticmethod
    def create_or_update_user(email: str, data: dict):
        body = {
            "email": email,
            "fullName": data.get("fullName"),
        }

        obj = UserModel.col().find_one_and_update({'email': email}, {'$set': body}, upsert=True, new=True)
        return obj
