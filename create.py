import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database specified by db_file
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

def add_country(conn, country):
    """ Create a new country into the countries table
    :param conn:
    :param country:
    :return: country id
    """
    sql = '''INSERT INTO countries(nazwa, kontynent, data_uzyskania_niepodległości) VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, country)
    conn.commit()
    return cur.lastrowid

def add_city(conn, city):
    """ Create a new city into the cities table
    :param conn:
    :param city:
    :return: city id
    """
    sql = '''INSERT INTO cities(country_id, nazwa, liczba_ludności, prawa_miejskie) VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, city)
    conn.commit()
    return cur.lastrowid

if __name__ == "__main__":
    country = ("Brazylia", "Ameryka Południowa", "1822-09-07")
    conn = create_connection("database.db")
    co_id = add_country(conn, country)

    city = (co_id, "Brasília", "2 817 068", "1962")
    city_id = add_city(conn, city)

    print(co_id, city_id)

    country2 = ("Francja", "Europa", "843-08-10")
    co_id2 = add_country(conn, country2)
    city2 = (co_id2, "Paryż", "2 148 271", "987")
    city_id2 = add_city(conn, city2)

    print(co_id2, city_id2)

    country3 = ("Portugalia", "Europa", "1128-06-24")
    co_id3 = add_country(conn, country3)
    city3 = (co_id3, "Lizbona", "505 526", "1484")
    city_id3 = add_city(conn, city3)

    print(co_id3, city_id3)

    country4 = ("Suazi", "Afryka", "1968-09-06")
    co_id4 = add_country(conn, country4)
    city4 = (co_id4, "Mbabane", "94 874", "1902")
    city_id4 = add_city(conn, city4)

    print(co_id4, city_id4)

    conn.close()
