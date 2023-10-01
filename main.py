from src.database import Database
from src.brick_sorter import BrickSorterApp


def main():
    db = Database()

    db.create_db()
    BrickSorterApp().run()
    db.close_db()


if __name__ == "__main__":
    main()
