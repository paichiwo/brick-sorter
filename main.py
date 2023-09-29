from src.database import Database
from src.brick_sorter import BrickSorter


def main():
    db = Database()
    db.create_db()
    BrickSorter().mainloop()
    db.close_db()


if __name__ == "__main__":
    main()
