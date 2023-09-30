import customtkinter as ctk


class CTkTableView(ctk.CTkScrollableFrame):
    def __init__(self, master, *args, values: list, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.values = values
        self.frames = []

        self.update_view()

    def clear(self):
        for frame in self.frames:
            frame.destroy()
        self.frames = []

    def insert_rows(self, data):
        self.clear()
        for item in data:
            frame = Frame(self, *item, fg_color="#02182b", height=50)
            frame.pack(fill='both', ipady=10, pady=5)
            self.frames.append(frame)

    def update_view(self):
        self.clear()
        self.insert_rows(self.values)


class Frame(ctk.CTkFrame):
    def __init__(self, master, part_number, part_name, color, amount, box, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.part_number = part_number
        self.part_name = part_name
        self.color = color
        self.amount = amount
        self.box = box

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.part_number_lbl = ctk.CTkLabel(self, text=f"{self.part_number} - {self.part_name}")
        self.part_color_lbl = ctk.CTkLabel(self, text=f"Color: {self.color}")
        self.part_amount_lbl = ctk.CTkLabel(self, text=f"Amount: {self.amount}")
        self.part_box_lbl = ctk.CTkLabel(self, text=f"Box: {self.box}")

        self.part_number_lbl.grid(row=0, column=0, sticky='we', columnspan=3, padx=10)
        self.part_color_lbl.grid(row=1, column=0, sticky='w', padx=10)
        self.part_amount_lbl.grid(row=1, column=1, padx=10)
        self.part_box_lbl.grid(row=1, column=2, sticky='e', padx=10)

