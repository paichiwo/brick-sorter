import sqlite3


class Database:
    def __init__(self):
        self.con = sqlite3.connect('db/inventory.db')
        self.cur = self.con.cursor()

    def create_db(self):
        with open('db/inventory.sql', 'r', encoding='utf-8') as sql_file:
            try:
                self.cur.executescript(sql_file.read())
                self.con.commit()
                print("Database created")
            except sqlite3.Error:
                print("Database exists, proceeding...")

    def close_db(self):
        self.con.close()

    def search_part(self, part_number):
        self.cur.row_factory = sqlite3.Row
        query = "SELECT * FROM Inventory WHERE part_number = ?"
        self.cur.execute(query, (part_number,))
        rows = self.cur.fetchall()
        if rows:
            result = [[row['part_number'], row['part_name'], row['color'], row['amount'], row['box']] for row in rows]
            return result

    def insert_part(self, part_number, part_name, part_color, part_amount, part_box):
        query = "INSERT INTO Inventory (part_number, part_name, color, amount, box) VALUES (?, ?, ?, ?, ?)"
        self.cur.execute(query, (part_number, part_name, part_color, part_amount, part_box))
        self.con.commit()
