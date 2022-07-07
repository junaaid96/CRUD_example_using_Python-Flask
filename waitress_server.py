import werkzeug.serving
from constants import Constants
from controllers.connector import app
from utils.database_utils import DatabaseUtils
from flask_cors import CORS


def run_server():
    cors = CORS(app)
    DatabaseUtils.init_local_db()
    werkzeug.run_simple('127.0.0.1', int(Constants.PORT), app, use_debugger=True, use_reloader=True)


if __name__ == '__main__':
    run_server()
