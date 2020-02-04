import mysql.connector as connector
from mysql.connector import Error

verbosity = 0


def start():

    try:
        connection = connector.connect(host="localhost",
                                       database="lanista",
                                       user="lanista_admin",
                                       password="password")

        if not connection.is_connected():
            print("Warning: Not connected.")
            raise connection.get_warnings()

        db_info = connection.get_server_info()
        if verbosity == 1:
            print("Connected to server with info:", db_info)

        cursor = connection.cursor()
        cursor.execute("use lanista;")
        warnings = cursor.fetchwarnings()
        if warnings != None or verbosity == 1:
            print("Warnings presented:", warnings)

    except Error as e:
        print("Error while connecting to MySQL:", e)
        return None, None

    finally:
        return connection, cursor


def run(connection, cursor):
    pass


if __name__ == "__main__":

    verbosity = 1

    connection, cursor = start()
    run(connection, cursor)