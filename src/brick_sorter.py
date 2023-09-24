import customtkinter as ctk


class BrickSorter(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title = "App"
        self.geometry("400x500")

    def gui(self):
        pass