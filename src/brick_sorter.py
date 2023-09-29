import webbrowser

import requests
import customtkinter as ctk
from PIL import Image
from src.helpers import rebrickable_api, create_part_image


class BrickSorter(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # -- WINDOW SETUP --
        self.title("Brick Sorter v0.01")
        self.geometry("400x320")
        self.configure(fg_color=("#BBBBBB", "#02182b"))
        self.resizable(False, False)
        ctk.set_default_color_theme("data/brick_sorter_theme.json")

        # -- LOGO --
        self.logo = ctk.CTkLabel(self, text="BRICK SORTER", text_color="#D7263D", font=("Any", 40, 'bold'))
        self.logo.pack(pady=10)

        # -- SEARCH FRAME --
        self.frame_s = ctk.CTkFrame(self)
        self.frame_s.pack(fill='x', padx=10)
        self.frame_s.columnconfigure(0, weight=1)

        self.search_entry = ctk.CTkEntry(self.frame_s, justify="center", font=("Any", 20, "bold"),
                                         placeholder_text="Search")
        self.search_entry.focus()
        self.search_entry.bind('<Return>', lambda event=None: self.search_btn.invoke())
        self.search_btn_img = ctk.CTkImage(Image.open("img/SEARCH_button.png"))
        self.search_btn = ctk.CTkButton(self.frame_s, image=self.search_btn_img, text="", width=18,
                                        command=self.search_part)

        self.search_entry.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10)
        self.search_btn.grid(row=0, column=2, padx=10, pady=10)

        # -- SEARCH RESULT FRAME
        self.frame_sr = ctk.CTkFrame(self)
        self.frame_sr.pack(fill='x', padx=10, pady=10)
        self.frame_sr.columnconfigure(0, weight=1)
        self.frame_sr.columnconfigure(1, weight=1)
        self.frame_sr.rowconfigure(0, weight=1)
        self.frame_sr.rowconfigure(1, weight=1)
        self.frame_sr.rowconfigure(2, weight=1)

        self.part_img = ctk.CTkImage(Image.open('img/placeholder.png'))
        self.part_img_lbl = ctk.CTkLabel(self.frame_sr, text="", image=self.part_img, width=100, height=100)
        self.part_number_lbl = ctk.CTkLabel(self.frame_sr, text="")
        self.part_name_lbl = ctk.CTkLabel(self.frame_sr, text="")
        self.part_url_btn = ctk.CTkButton(self.frame_sr, text="", fg_color='transparent', width=50)

        self.part_img_lbl.grid(row=0, column=0, rowspan=3, padx=10)
        self.part_number_lbl.grid(row=0, column=1, padx=10)
        self.part_name_lbl.grid(row=1, column=1, padx=10)
        self.part_url_btn.grid(row=2, column=1, padx=10)

        # -- USER INPUT FRAME --
        self.frame_ui = ctk.CTkFrame(self, height=100)
        self.frame_ui.pack(fill='x', padx=10)
        self.frame_ui.columnconfigure(0, weight=1)
        self.frame_ui.columnconfigure(1, weight=1)
        self.frame_ui.columnconfigure(2, weight=1)

        self.box_entry = ctk.CTkEntry(self.frame_ui, placeholder_text="Box number")
        self.add_btn = ctk.CTkButton(self.frame_ui, text="Add")
        self.del_btn = ctk.CTkButton(self.frame_ui, text="Delete")

        self.box_entry.grid(row=0, column=0, padx=10, pady=10)
        self.add_btn.grid(row=0, column=1)
        self.del_btn.grid(row=0, column=2, padx=10)

        # -- MESSAGE FRAME --
        self.message = ctk.CTkLabel(self, text="")
        self.message.pack(side='bottom')

    def search_part(self):
        try:
            part_img_url, part_number, part_name, part_url = rebrickable_api(self.search_entry.get())
            image = create_part_image(part_img_url)

            self.part_img_lbl.configure(image=image)
            self.part_number_lbl.configure(text=part_number)
            self.part_name_lbl.configure(text=part_name)
            self.part_url_btn.configure(text="Bricklink", font=('Any', 12, 'underline'),
                                        command=lambda: webbrowser.open(part_url))
        except (requests.exceptions.RequestException, requests.exceptions.JSONDecodeError):
            self.message.configure(text="Connection Error")
        except KeyError:
            self.message.configure(text="Part doesn't exist")
