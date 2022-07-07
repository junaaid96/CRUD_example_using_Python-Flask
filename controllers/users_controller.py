from datetime import datetime, timezone

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, get_jwt
from db_models.blocked_token_model import BlockedTokenModel
from services.user_service import UserService
from utils.data_utils import DataUtils
from utils.responder import Responder

users_controller = Blueprint('users', __name__)


@users_controller.route('/')
def root():
    return Responder.ok(UserService.get_users())

@users_controller.route('/test')
def test():
    return "TETE"


@users_controller.get('/auth_test')
@jwt_required()
def auth_test():
    current_user = get_jwt_identity()
    return current_user


@users_controller.post('/login')
def login_test():
    body = request.form.to_dict()
    email = body.get('email')
    logged_in_user = DataUtils.create_or_update_user(email, body)
    identity = str(logged_in_user.get('_id'))
    access_token = create_access_token(identity)

    to_be_returned = {
        "access_token": access_token,
    }
    return to_be_returned


@users_controller.delete('/logout')
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    now = datetime.now(timezone.utc)

    BlockedTokenModel.col().insert_one({
        "jti": jti,
        "created_at": now,
    })
    return Responder.ok({"success": True})
