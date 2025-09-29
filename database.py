import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "admin"
        self.database = "desarrollo_web"
    
    def get_connection(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if connection.is_connected():
                return connection
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
            return None
    
    def execute_query(self, query, params=None):
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                connection.commit()
                return cursor
            except Error as e:
                print(f"Error ejecutando query: {e}")
                return None
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
    
    def fetch_all(self, query, params=None):
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                result = cursor.fetchall()
                return result
            except Error as e:
                print(f"Error obteniendo datos: {e}")
                return []
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
    
    def fetch_one(self, query, params=None):
        connection = self.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                result = cursor.fetchone()
                return result
            except Error as e:
                print(f"Error obteniendo dato: {e}")
                return None
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()