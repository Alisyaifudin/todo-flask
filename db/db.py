import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
import os
load_dotenv()

config = {
  'user': os.getenv("DATABASE_USER"),
  'password': os.getenv("DATABASE_PASSWORD"),
  'host': os.getenv("DATABASE_HOST"),
  'database': os.getenv("DATABASE_NAME"),
  'raise_on_warnings': True
}

def connection():
    print("Connected to database")
    return mysql.connector.connect(**config)

try:
    cnx = connection
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
    cnx = None