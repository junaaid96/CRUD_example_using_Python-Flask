import json
from flask import Response


class Responder:

    @staticmethod
    def ok(data):
        return Response(json.dumps(data, default=str), mimetype="application/json", status=200)

    @staticmethod
    def error_not_found(data):
        return Response(json.dumps(data, default=str), mimetype="application/json", status=404)

    @staticmethod
    def error_unauthorized():
        return Response("UNAUTHORIZED", status=403)
