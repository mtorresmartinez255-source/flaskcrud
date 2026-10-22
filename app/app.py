from flask import Flask
import pymysql

# Forzamos a pymysql a actuar como MySQLdb para evitar errores de compilación
pymysql.install_as_MySQLdb()

# Application initializations
app = Flask(__name__)

# settings
app.secret_key = "mysecretkey"