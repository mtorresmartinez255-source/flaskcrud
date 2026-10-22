from app import app
from dotenv import load_dotenv
import os
import pymysql

load_dotenv()

# Clase que simula exactamente el comportamiento de Flask-MySQLdb usando PyMySQL puro
class MySQLConnectionManager:
    def __init__(self, app=None):
        pass
    @property
    def connection(self):
        return pymysql.connect(
            host=os.getenv('MYSQL_HOST', 'db'), # Apunta al contenedor de la base de datos
            user=os.getenv('MYSQL_USER', 'root'),
            password=os.getenv('MYSQL_PASSWORD', 'tu_password'),
            database=os.getenv('MYSQL_DB', 'tu_base_de_datos'),
            cursorclass=pymysql.cursors.DictCursor
        )

# Creamos la instancia 'mysql' para que devuelva la conexión como propiedad
mysql = MySQLConnectionManager(app)