import tkinter
import customtkinter as ctk
from PIL import Image
from CTkScrollableDropdown import CTkScrollableDropdown
from CTkTableView import CTkTableView
from src.helpers import read_lego_colors


class Gui(ctk.CTk):
    """This class contains all the UI elements for the Brick Sorter"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.part_nb = tkinter.StringVar()
        self.part_nm = tkinter.StringVar()

        # -- WINDOW SETUP --
        self.title("Brick Sorter v0.01")
        self.geometry("450x250")
        self.configure(fg_color=("#BBBBBB", "#02182b"))
        ctk.set_default_color_theme("data/brick_sorter_theme.json")

        # -- LOGO --
        self.logo = ctk.CTkLabel(self, text="BRICK SORTER", text_color="#D7263D", font=("Any", 40, 'bold'))
        self.logo.pack(pady=10)

        # -- SEARCH FRAME --
        self.frame_s = ctk.CTkFrame(self, fg_color="transparent")
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

        # -- USER INPUT FRAME --
        self.frame_ui = ctk.CTkFrame(self, height=100)
        self.frame_ui.pack(fill='x', padx=10, pady=10)
        self.frame_ui.columnconfigure(0, weight=1)
        self.frame_ui.columnconfigure(1, weight=1)
        self.frame_ui.columnconfigure(2, weight=1)
        self.frame_ui.columnconfigure(3, weight=1)

        self.color = ctk.CTkOptionMenu(self.frame_ui)
        self.color.set("No color")
        CTkScrollableDropdown(self.color, values=read_lego_colors(), font=("Any", 10),
                              button_color=("grey92", "#021f37"), hover_color="#d7263d",
                              frame_border_width=1, justify="left", width=180)

        self.amount = ctk.CTkEntry(self.frame_ui, placeholder_text="Amount", width=50)
        self.box_entry = ctk.CTkEntry(self.frame_ui, placeholder_text="Box", width=50)
        self.add_btn = ctk.CTkButton(self.frame_ui, text="Add", command=self.add_part)
        self.del_btn = ctk.CTkButton(self.frame_ui, text="Delete", command=self.delete_part)

        self.color.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="we")
        self.amount.grid(row=0, column=2, padx=10, sticky="we")
        self.box_entry.grid(row=0, column=3, padx=10, sticky="we")
        self.add_btn.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="we")
        self.del_btn.grid(row=1, column=2, columnspan=2, padx=10, sticky="we")

        # -- SEARCH RESULT FRAME
        self.frame_sr = ctk.CTkFrame(self, fg_color="transparent", height=120)
        self.frame_sr.columnconfigure(0, weight=1)
        self.frame_sr.columnconfigure(1, weight=1)
        self.frame_sr.rowconfigure(0, weight=1)
        self.frame_sr.rowconfigure(1, weight=1)
        self.frame_sr.rowconfigure(2, weight=1)

        self.part_img = ctk.CTkImage(Image.open('img/placeholder.png'))
        self.part_img_lbl = ctk.CTkLabel(self.frame_sr, text="", image=self.part_img, width=100, height=100)
        self.part_number_lbl = ctk.CTkLabel(self.frame_sr, textvariable=self.part_nb)
        self.part_name_lbl = ctk.CTkLabel(self.frame_sr, text="")
        self.part_url_btn = ctk.CTkButton(self.frame_sr, text="", fg_color='transparent', width=50)

        self.part_img_lbl.grid(row=0, column=0, rowspan=3, padx=20, sticky='w')
        self.part_number_lbl.grid(row=0, column=1, padx=10, pady=10)
        self.part_name_lbl.grid(row=1, column=1, padx=10)
        self.part_url_btn.grid(row=2, column=1, padx=10, pady=10)

        # -- DB SEARCH RESULT FRAME --
        self.table = CTkTableView(self, values=[], height=180)

        # -- MESSAGE ELEMENT --
        self.message = ctk.CTkLabel(self, text="")
        self.message.pack(side='bottom')
