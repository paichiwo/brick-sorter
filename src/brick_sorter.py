import sqlite3
import webbrowser
import requests
from src.gui import Gui
from src.database import Database
from src.helpers import rebrickable_api, create_part_image, part_name_shortener


class BrickSorterApp(Gui):
    """Logic for the Brick Sorter"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db = Database()

    def run(self):
        """Run the app"""
        self.mainloop()

    def update_table(self, part_number, pack=False):
        """Update the table"""
        self.table.clear()
        if self.db.search_part(part_number):
            self.table.insert_rows(self.db.search_part(part_number))
        if pack:
            self.table.pack(fill='x', padx=10, pady=10)

    def search_part(self):
        """Search part online and in the database and display results"""
        try:
            part_img_url, part_number, part_name, part_url = rebrickable_api(self.search_entry.get())
            if part_img_url and part_number and part_name and part_url:
                self.geometry("450x600")
                self.frame_sr.pack(fill='x', padx=10)
                self.message.configure(text="")
                self.table.clear()

                self.part_img_lbl.configure(image=create_part_image(part_img_url))
                self.part_nb.set(part_number)
                self.part_nm.set(part_name)
                self.part_name_lbl.configure(text=part_name_shortener(part_name))
                self.part_url_btn.configure(text="Bricklink", command=lambda: webbrowser.open(part_url))
                self.update_table(part_number, pack=True)
        except (requests.exceptions.RequestException, requests.exceptions.JSONDecodeError):
            self.message.configure(text="Connection Error")
        except KeyError:
            self.message.configure(text="Part doesn't exist")

    def add_part(self):
        """Add part to the database"""
        part_number = self.part_nb.get()
        part_name = self.part_nm.get()
        part_color = self.color.get()
        part_amount = self.amount.get()
        part_box = self.box_entry.get().upper()

        if all([part_number and part_name and part_color and part_amount and part_box]):
            try:
                self.handle_add_part(part_number, part_name, part_color, part_amount, part_box)
                self.update_table(part_number)
            except sqlite3.Error as e:
                self.message.configure(text=f"Error inserting part: {e}")
        else:
            self.message.configure(text="Please enter all of the values")

    def handle_add_part(self, part_number, part_name, part_color, part_amount, part_box):
        if not self.db.check_existing(part_number, part_color):
            self.db.insert_part(part_number, part_name, part_color, part_amount, part_box)
            self.message.configure(text="Part inserted successfully")
        else:
            self.message.configure(text=f"Part: {part_number} with color: {part_color} exists in the database")

    def delete_part(self):
        """Delete part from the database"""
        values = self.table.get_values()
        if values:
            try:
                self.handle_delete_part(values["part_number"], values["part_color"])
                self.update_table(values["part_number"])
            except sqlite3.Error as e:
                self.message.configure(text=f"Error deleting part: {e}")

    def handle_delete_part(self, part_number, part_color):
        check_deleted = self.db.delete_part(part_number, part_color)
        if check_deleted == 0:
            self.message.configure(text="No matching part found")
        elif check_deleted == 1:
            self.message.configure(text="Part deleted successfully")
        else:
            self.message.configure(text=f"Unexpected number of rows deleted: {check_deleted}")
