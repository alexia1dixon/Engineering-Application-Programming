import serial
from serial import Serial

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

# cc3220sf = serial.Serial('COM4', 115200) #(port number, baudrate) - create a serial object
with serial.Serial('COM4', 115200, timeout=10) as cc3220sf:
  line = cc3220sf.readlines()

print(line)

if __name__ == '__main__':
    create_connection(r"pythonsqlite.db")
