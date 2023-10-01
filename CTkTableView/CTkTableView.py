import customtkinter as ctk


class CTkTableView(ctk.CTkScrollableFrame):
    def __init__(self, master, *args, values: list, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.values = values
        self.frames = []

        self.update_view()

    def clear(self):
        """Clear all the frames"""
        for frame in self.frames:
            frame.destroy()
        self.frames = []

    def insert_rows(self, data):
        """Insert data into the table"""
        self.clear()
        for item in data:
            frame = Frame(self, *item, fg_color="#02182b", height=50)
            frame.pack(fill='both', ipady=10, pady=5)
            self.frames.append(frame)

    def get_values(self):
        """Returns the values of the selected frame, or None if no frame is selected."""
        selected_frame = self.get_selected_frame()
        if selected_frame is not None:
            return selected_frame.get_values()
        else:
            return None

    def get_selected_frame(self):
        """Returns the selected frame, or None if no frame is selected."""
        for frame in self.frames:
            if frame.cget("fg_color") == "#d7263d":
                return frame
        return None

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

        self.selected_frame = None
        self.bind("<Button-1>", self.select)
        self.bind("<Button-3>", self.deselect)

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

    def select(self, event):
        """Action when frame selected - left mouse button"""
        # Deselect all frames first
        for frame in self.master.frames:
            frame.configure(fg_color="#02182b")
        # Select the clicked frame
        self.configure(fg_color="#d7263d")

    def deselect(self, event):
        """Action when frame deselected - right mouse button"""
        for frame in self.master.frames:
            frame.configure(fg_color="#02182b")

    def get_values(self):
        """Return values of selected frame"""
        return {"part_number": self.part_number,
                "part_name": self.part_name,
                "part_color": self.color,
                "part_amount": self.amount,
                "part_box": self.box}
