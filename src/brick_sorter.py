import requests
import customtkinter as ctk
from PIL import Image
from src.helpers import rebrickable_api, create_part_image


class BrickSorter(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.logo = None
        self.frame_s = None
        self.search_s = None
        self.button_img = None
        self.button_s = None
        self.frame_sr = None
        self.image_sr = None
        self.image_lbl = None

        self.message = None

        self.title("Brick Sorter v0.01")
        self.geometry("600x400")
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

        self.search_s = ctk.CTkEntry(self.frame_s, justify="center", font=("Any", 20, "bold"))
        self.button_img = ctk.CTkImage(Image.open("img/SEARCH_button.png"))
        self.button_s = ctk.CTkButton(self.frame_s, image=self.button_img, text="", width=18, command=self.search_part)
        self.search_s.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10)
        self.button_s.grid(row=0, column=2, padx=10, pady=10)

        self.search_s.bind('<Return>', lambda event=None: self.button_s.invoke())
        self.search_s.focus()

    def search_result_frame(self):
        self.frame_sr = ctk.CTkFrame(self)
        self.frame_sr.pack(fill='x', padx=10, pady=10)

        self.image_sr = ctk.CTkImage(Image.open('img/placeholder.png'))
        self.image_lbl = ctk.CTkLabel(self.frame_sr, text="", image=self.image_sr, width=100, height=100)
        self.image_lbl.pack(anchor='w', padx=10)

    def message_label(self):
        self.message = ctk.CTkLabel(self, text="test")
        self.message.pack()

    def search_part(self):
        try:
            part_img_url, part_number, part_name, part_url = rebrickable_api(self.search_s.get())
            image = create_part_image(part_img_url)
            self.image_lbl.configure(image=image)
            self.image_lbl['image'] = image

            print(part_number)
            print(part_name)
            print(part_url)
        except (requests.exceptions.RequestException, requests.exceptions.JSONDecodeError):
            self.message.configure(text="Connection Error.")
