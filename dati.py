import sqlite3


conn = sqlite3.connect("dati.db", check_same_thread=False)


def lietotaju_tabulas_izveide():
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT NOT NULL,
        uzvards TEXT NOT NULL,
        lietotajvards TEXT NOT NULL UNIQUE
        )
        """
    )
    conn.commit()

def zinojumu_tabulas_izveide():
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE zinojumi(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        userid INTEGER NOT NULL,
        zinojums TEXT NOT NULL,
        FOREIGN KEY(userid) REFERENCES users(id)
        )
        """
    )
    conn.commit()

# lietotaju_tabulas_izveide()
# zinojumu_tabulas_izveide()

def add_user(vards, uzvards, lietotajvards):
    print(vards, uzvards)
    cur = conn.cursor()
    cur.execute(
        f"""
        INSERT INTO users(vards, uzvards, lietotajvards) VALUES("{vards}","{uzvards}","{lietotajvards}")
        """
    )
    conn.commit()

def add_message(zinojums, id):
    print(zinojums)
    cur = conn.cursor()
    cur.execute(
        f"""
        INSERT INTO zinojumi(zinojums, userid) VALUES("{zinojums}","{id}")
        """
    )
    conn.commit()



def iegut_zinojumus():
    cur = conn.cursor()
    cur.execute(
        """SELECT vards, uzvards, zinojums FROM users JOIN zinojumi ON userid=users.id"""
    )
    conn.commit()
    dati = cur.fetchall()
    return dati

def iegut_lietotaju():
    cur = conn.cursor()
    cur.execute(
        """SELECT lietotajvards, id FROM users ORDER BY lietotajvards ASC"""
    )
    conn.commit()
    dati = cur.fetchall()
    return dati