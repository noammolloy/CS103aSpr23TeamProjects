import sqlite3

class Transaction:
    def __init__(self, filename) -> None:
        con= sqlite3.connect(filename)
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY, item# int, amount int, category text, date text, description text)")
        con.commit()
        con.close()

    
