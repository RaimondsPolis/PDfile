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
        zinojums TEXT NOT NULL
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