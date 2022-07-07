import certifi
from mongoengine import connect

from utils.logger import Logger


class DatabaseUtils:
    @staticmethod
    def init_local_db(database_name="py_project1"):
        alias = connect(database_name)
        Logger.log_including_time("database_utils", "init_local_db", f"database_name: {database_name}")

    @staticmethod
    def init_cluster_db(MONGO_URI, database_name="py_project1"):
        ca = certifi.where()
        alias = connect(database_name, host=MONGO_URI, tlsCAFile=ca)
        Logger.log_including_time("database_utils", "init_local_db", f"MONGO_URI: {MONGO_URI}",
                                  f"database_name: {database_name}")
