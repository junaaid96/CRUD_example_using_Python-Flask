from db_models.user_model import UserModel


class UserService:

    @staticmethod
    def create_user():
        UserModel.col().insert_one({
            "name": "FF",
            "email": "EE",
            "password": "PP",
        })

    @staticmethod
    def get_users():
        return list(UserModel.col().find({}))
