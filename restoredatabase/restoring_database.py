import psycopg2
from config import config

config = config()


class ConnectionDatabase(object):
    def __init__(self):
        self.db_params = config

    def connect_database(self):
        try:
            connection = psycopg2.connect(**self.db_params)
        except Exception as e:
            print(e)

        return connection


def restore_database(connection_db, file_restore):
    cur = connection_db.cursor()
    with open(file_restore, 'r') as file_sql:
        data = file_sql.read()
        cur.execute(data)
        connection_db.commit()
        connection_db.close()
