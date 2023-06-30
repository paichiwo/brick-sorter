import json
import os
import sys
from tkinter import *
from tkinter import messagebox, Label, PhotoImage, Entry

import requests

colors = ["#D7263D", "#02182B", "#0197F6", "#448FA3", "#68C5DB"]
catalog = {}


def resource_path(relative_path):
    """PyInstaller requirement,
    Get an absolute path to resource, works for dev and for PyInstaller."""
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def get_api_key():
    """Read API key from file."""
    with open("api.txt") as f:
        key = f.read()
    return key


def rebrickable_api(part_num):
    """Get lego part information from rebrickable.com."""
    key = get_api_key()
    url = f"https://rebrickable.com/api/v3/lego/parts/{part_num}/?key={key}"
    lego_data = requests.get(url).json()

    part_number = lego_data["part_num"]
    part_name = lego_data["name"]
    year = (lego_data["year_from"], lego_data["year_to"])
    part_img_url = lego_data["part_img_url"]

    bricklink_id = lego_data["external_ids"]["BrickLink"][0]
    part_url = f"https://www.bricklink.com/v2/catalog/catalogitem.page?P={bricklink_id}#T=C"

    return part_number, part_name, year, part_img_url, part_url


def update_window():
    search_term = entry_box.get()
    print(rebrickable_api(search_term))


def add_to_catalog():
    pass


def save_catalog():
    with open('catalog.json', 'w') as file:
        json.dump(catalog, file)
    messagebox.showinfo("Success", "Catalog saved.")


def load_catalog():
    global catalog
    try:
        with open('catalog.json', 'r') as file:
            catalog = json.load(file)
    except FileNotFoundError:
        catalog = {}



# Create a window and widgets
root = Tk()
root.title("Lego Sorter")
root.resizable(False, False)
root.configure(bg=colors[1])

# Set the window geometry
window_width = 540
window_height = 400
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Calculate the x and y coordinates to center the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
# Set the window's position
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

background_image = PhotoImage(file=resource_path("images/background.png"))
background_label = Label(root, image=background_image, borderwidth=0)
background_label.pack()

app_name = Label(text="BRICK SORTER", font=("Manrope ExtraBold", 27), bg=colors[1], fg=colors[0])
app_name.place(x=140, y=0)

entry_box = Entry(root, justify='center', width=12, font=('Manrope', 14),
                  bg=colors[0], border=0, fg='white')
entry_box.pack()
entry_box.place(x=200, y=57, height=25)
entry_box.focus()

search_button_image = PhotoImage(file=resource_path("images/SEARCH button.png"))
search_button = Button(image=search_button_image, borderwidth=0, bg=colors[0], activebackground=colors[0],
                       command=update_window)
search_button.place(x=370, y=58)

part_drawing_image = PhotoImage(file=resource_path("images/dummy_picture.png"))
part_drawing_label = Label(image=part_drawing_image)
part_drawing_label.place(x=220, y=101)

part_number_label = Label(text="3022", justify="center", font=("Manrope", 10, 'bold'), bg=colors[1], fg='white', height=1)
part_number_label.place(x=121, y=209, width=300)

part_name_label = Label(text="Plate 2x2", justify="center", font=("Manrope", 10, 'bold'), bg=colors[1], fg='white', height=1)
part_name_label.place(x=121, y=229, width=300)

part_year_label = Label(text="(1982, 2023)", justify="center", font=("Manrope", 10, 'bold'), bg=colors[1], fg='white', height=1)
part_year_label.place(x=121, y=249, width=300)

part_year_label = Label(text="Bricklink", justify="center", font=("Manrope", 10, 'bold'), bg=colors[1], fg='white', height=1)
part_year_label.place(x=121, y=269, width=300)

box_label = Label(text="BOX: A", justify="center", font=("Manrope ExtraBold", 11), bg=colors[1], fg='white', height=1)
box_label.place(x=121, y=300, width=300)

add_button_image = PhotoImage(file=resource_path("images/ADD button.png"))
add_button = Button(image=add_button_image, borderwidth=0, bg=colors[1], activebackground=colors[1])
add_button.place(x=143, y=323)

delete_button_image = PhotoImage(file=resource_path("images/DELETE button.png"))
delete_button = Button(image=delete_button_image, borderwidth=0, bg=colors[1], activebackground=colors[1])
delete_button.place(x=323, y=323)

root.mainloop()


# if __name__ == "__main__":
#     main()
