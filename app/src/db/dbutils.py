from mysql.connector import MySQLConnection
from mysql.connector import connect
import app.config as cfg

def get_db_cnx() -> MySQLConnection:
    return connect(**cfg.db_config)
