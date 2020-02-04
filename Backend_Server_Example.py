import mysql.connector as connector
from mysql.connector import Error

verbosity = 1
connection = None
cursor = None


try:
    connection = connector.connect(host="localhost",
                                   database="lanista",
                                   user="lanista_admin",
                                   password="password")

    if (not connection.is_connected()):
        print("Warning: Not connected.")
        raise connection.get_warnings()

    db_info = connection.get_server_info()
    print("Connected to server with info:", db_info)
    cursor = connection.cursor()
    cursor.execute("use lanista;")
    warnings = cursor.fetchwarnings()
    if (warnings != None or verbosity == 1):
        print("Warnings presented:", warnings)
    cursor.execute("SELECT * FROM videos;")


except Error as e:
    print("Error while connecting to MySQL:", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")


if __name__ == "__main__":
    print("Hello World!")