from flask import Blueprint, request
from constants import Constants
from services.root_services import RootService
from utils.responder import Responder

root_controller = Blueprint('main', __name__)


@root_controller.get('/')
def get_all():
    return Responder.ok(RootService.get_all())

@root_controller.get('/one')
def get_one():
    data = request.args.to_dict()
    return Responder.ok(RootService.get_one(data))

@root_controller.post('/')
def create_one():
    data = request.form.to_dict()
    RootService.create(data)
    return "created"

@root_controller.put('/')
def update():
    query = request.args.to_dict()
    body = request.form.to_dict()
    Responder.ok(RootService.update(query, body))
    return "updated"

@root_controller.delete('/')
def delete_one():
    query = request.args.to_dict()
    Responder.ok(RootService.delete_one(query))
    return "deleted"

@root_controller.delete('/del')
def delete_all():
    RootService.delete_all()
    return "all deleted"