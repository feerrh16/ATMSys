# db.py
import psycopg2
from psycopg2 import sql

def connect():
    return psycopg2.connect(
        dbname="ATMSys",
        user="postgres",
        password="Password",
        host="127.0.0.1",
        port="5432"
    )

def execute_query(query, params=None):
    conn = connect()
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    cur.close()
    conn.close()

def fetch_query(query, params=None):
    conn = connect()
    cur = conn.cursor()
    cur.execute(query, params)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result
