from src.database import Database
from src.brick_sorter import BrickSorter


def main():
    db = Database()
    db.create_db()
    BrickSorter().mainloop()


if __name__ == "__main__":
    main()
