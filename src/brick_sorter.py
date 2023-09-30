import sqlite3
import webbrowser
import requests
from src.gui import Gui
from src.database import Database
from src.helpers import rebrickable_api, create_part_image


class BrickSorter(Gui):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db = Database()

    def search_part(self):
        try:
            part_img_url, part_number, part_name, part_url = rebrickable_api(self.search_entry.get())
            if part_img_url and part_number and part_name and part_url:
                self.geometry("440x600")
                self.frame_sr.configure(fg_color="#021f37")
                self.frame_sr.pack(fill='x', padx=10)
                self.message.configure(text="")

                self.part_img_lbl.configure(image=create_part_image(part_img_url))
                self.part_nb.set(part_number)
                self.part_nm.set(part_name)
                self.part_url_btn.configure(text="Bricklink", command=lambda: webbrowser.open(part_url))

                search_result = self.db.search_part(part_number)
                if search_result:
                    self.table.insert_rows(search_result)
                    self.table.pack(fill='x', padx=10, pady=10)

        except (requests.exceptions.RequestException, requests.exceptions.JSONDecodeError):
            self.message.configure(text="Connection Error")
        except KeyError:
            self.message.configure(text="Part doesn't exist")

    def add_part(self):
        part_number = self.part_nb.get()
        part_name = self.part_nm.get()
        part_color = self.color.get()
        part_amount = self.amount.get()
        part_box = self.box_entry.get().upper()

        if part_number and part_name and part_color and part_amount and part_box:
            try:
                part_exists = self.db.check_existing(part_number, part_color)
                if not part_exists:
                    self.db.insert_part(part_number, part_name, part_color, part_amount, part_box)
                    self.message.configure(text="Part inserted successfully")
                else:
                    self.message.configure(text=f"Part: {part_number} with color: {part_color} exists in the database")
            except sqlite3.Error as e:
                self.message.configure(text=f"Error inserting part: {e}")
        else:
            self.message.configure(text="Please enter all of the values")

    def delete_part(self):
        print(self.table.get_values())
