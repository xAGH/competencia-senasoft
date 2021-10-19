from pymysql import Connection, connect, MySQLError

class Connection:

    mysql: Connection

    @classmethod
    def open_connection(cls):
        try:
            pass
        except MySQLError as me:
            pass
        except Exception as e:
            pass