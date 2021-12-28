import mysql.connector
from utilities.common_ops import CommonOps

my_db = None


class ManageDB:

    @staticmethod
    def setup_db_connection():
        my_db = mysql.connector.connect(
            host="sql11.freemysqlhosting.net",
            database="sql11461525",
            user="sql11461525",
            password="macr6ThbXd",
        )

        globals()['my_db'] = my_db

    @staticmethod
    def close_connection():
        my_db.close()

    @staticmethod
    def get_db_data():
        query = CommonOps.get_data("Select")
        my_cursor = my_db.cursor()
        my_cursor.execute(query)
        my_result = my_cursor.fetchall()
        return my_result