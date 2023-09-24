import requests
import customtkinter as ctk
from src.helpers import get_api_key


class BrickSorter(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.search = None
        self.button = None
        self.message = None

        self.title("App")
        self.geometry("400x500")

        self.gui()

    def gui(self):
        self.search = ctk.CTkEntry(self)
        self.search.pack()
        self.button = ctk.CTkButton(self, text="Search", command=self.search_part)
        self.button.pack()
        self.message = ctk.CTkLabel(self, text="")
        self.message.pack()

    def search_part(self):
        part_img_url, part_number, part_name, part_url = self.rebrickable_api(self.search.get())
        print(part_img_url)
        print(part_number)
        print(part_name)
        print(part_url)

    def rebrickable_api(self, part_num):
        """Return lego part information from rebrickable.com API."""
        key = get_api_key()
        url = f'https://rebrickable.com/api/v3/lego/parts/{part_num}/?key={key}'
        try:
            if requests.get(url).status_code == 200:
                lego_data = requests.get(url).json()

                part_img_url = lego_data['part_img_url']
                part_number = lego_data['part_num']
                part_name = lego_data['name']

                bricklink_id = lego_data['external_ids']['BrickLink'][0]
                part_url = f'https://www.bricklink.com/v2/catalog/catalogitem.page?P={bricklink_id}#T=C'

                return part_img_url, part_number, part_name, part_url
            else:
                self.message.configure(text="API Error.")
        except (requests.exceptions.HTTPError,
                requests.exceptions.ConnectionError,
                requests.exceptions.JSONDecodeError):
            self.message.configure(text="Connection Error.")

