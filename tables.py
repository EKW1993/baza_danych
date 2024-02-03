import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def execute_sql(conn, sql):
    """Execute sql
    :param conn: Connection object
    :param sql: a SQL script
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

if __name__ == "__main__":
    create_countries_sql = """ 
    -- countries table
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY,
        nazwa TEXT NOT NULL,
        kontynent TEXT,
        data_uzyskania_niepodległości TEXT
    );
    """

    create_cities_sql = """
    -- city table
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY,
        country_id INTEGER NOT NULL,
        nazwa VARCHAR(250) NOT NULL,
        liczba_ludności INTEGER NOT NULL,
        prawa_miejskie TEXT NOT NULL,
        FOREIGN KEY (country_id) REFERENCES countries (id)
    );
    """

    db_file = "database.db"

    conn = create_connection(db_file)
    if conn is not None:
        execute_sql(conn, create_countries_sql)
        execute_sql(conn, create_cities_sql)
        conn.close()