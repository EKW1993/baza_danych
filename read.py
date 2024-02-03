import sqlite3

def create_connection(db_file):
    """
    create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
        return conn


def select_all_countries(conn):
    """
    Query all rows in the countries table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM countries")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_all_cities(conn):
    """
    Query all rows in the cities table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM cities")
    rows = cur.fetchall()
    for row in rows:
        print(row)

if __name__ == "__main__":
    db_file = "database.db"
    conn = create_connection(db_file)
    select_all_countries(conn)
    select_all_cities(conn)
    conn.close()