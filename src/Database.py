import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect('db/inventory.db')
        self.cur = self.con.cursor()

    def create_db(self):
        with open('db/inventory.sql') as sql_file:
            sql_script = sql_file.read()
            self.cur.executescript(sql_script)
        self.con.commit()

