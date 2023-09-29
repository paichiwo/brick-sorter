import webbrowser

import requests
import customtkinter as ctk
from PIL import Image
from src.helpers import rebrickable_api, create_part_image, open_link


class BrickSorter(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.logo = None
        self.frame_s = None
        self.search_entry = None
        self.search_button_img = None
        self.search_button = None
        self.frame_sr = None
        self.part_image = None
        self.part_image_lbl = None
        self.part_number_lbl = None
        self.part_name_lbl = None
        self.part_url_btn = None

        self.message = None

        self.title("Brick Sorter v0.01")
        self.geometry("400x400")
        self.configure(fg_color=("#BBBBBB", "#02182b"))
        ctk.set_default_color_theme("data/brick_sorter_theme_v0.1.json")

        self.logo_label()
        self.search_frame()
        self.search_result_frame()
        self.message_label()

    def logo_label(self):
        self.logo = ctk.CTkLabel(self, text="BRICK SORTER", text_color="#D7263D", font=("Arial", 40, 'bold'))
        self.logo.pack(pady=10)

    def search_frame(self):

        self.frame_s = ctk.CTkFrame(self)
        self.frame_s.pack(fill='x', padx=10)
        self.frame_s.columnconfigure(0, weight=1)

        self.search_entry = ctk.CTkEntry(self.frame_s, justify="center", font=("Any", 20, "bold"))
        self.search_button_img = ctk.CTkImage(Image.open("img/SEARCH_button.png"))
        self.search_button = ctk.CTkButton(self.frame_s, image=self.search_button_img, text="", width=18, command=self.search_part)
        self.search_entry.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10)
        self.search_button.grid(row=0, column=2, padx=10, pady=10)

        self.search_entry.focus()
        self.search_entry.bind('<Return>', lambda event=None: self.search_button.invoke())

    def search_result_frame(self):
        
        self.frame_sr = ctk.CTkFrame(self)
        self.frame_sr.pack(fill='x', padx=10, pady=10)
        self.frame_sr.columnconfigure(0, weight=1)
        self.frame_sr.columnconfigure(1, weight=1)
        self.frame_sr.rowconfigure(0, weight=1)
        self.frame_sr.rowconfigure(1, weight=1)
        self.frame_sr.rowconfigure(2, weight=1)

        self.part_image = ctk.CTkImage(Image.open('img/placeholder.png'))

        self.part_image_lbl = ctk.CTkLabel(self.frame_sr, text="", image=self.part_image, width=100, height=100)
        self.part_number_lbl = ctk.CTkLabel(self.frame_sr, text="")
        self.part_name_lbl = ctk.CTkLabel(self.frame_sr, text="")
        self.part_url_btn = ctk.CTkButton(self.frame_sr, text="", fg_color='transparent', width=50)

        self.part_image_lbl.grid(row=0, column=0, rowspan=3, sticky='w', padx=10)
        self.part_number_lbl.grid(row=0, column=1, padx=10)
        self.part_name_lbl.grid(row=1, column=1, padx=10)
        self.part_url_btn.grid(row=2, column=1, padx=10)

    def message_label(self):
        self.message = ctk.CTkLabel(self, text="test")
        self.message.pack()

    def search_part(self):
        try:
            part_img_url, part_number, part_name, part_url = rebrickable_api(self.search_entry.get())
            image = create_part_image(part_img_url)

            self.part_image_lbl.configure(image=image)
            self.part_number_lbl.configure(text=part_number)
            self.part_name_lbl.configure(text=part_name)
            self.part_url_btn.configure(text="Bricklink", font=('Any', 12, 'underline'), command=lambda: webbrowser.open(part_url))
        except (requests.exceptions.RequestException, requests.exceptions.JSONDecodeError):
            self.message.configure(text="Connection Error.")

