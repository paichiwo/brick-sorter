import io
import json
import os
import sys
import requests
import webbrowser
from urllib.request import urlopen
from rembg import remove
from PIL import Image as img
from PIL import ImageTk as imgtk
from tkinter import Tk, Button, Label, PhotoImage, Entry, messagebox, StringVar
from tkextrafont import Font


colors = ['#D7263D', '#02182B', '#0197F6', '#448FA3', '#68C5DB', '#FFFFFF']
catalog = {}


def resource_path(relative_path):
    """PyInstaller requirement,
    Get an absolute path to resource, works for dev and for PyInstaller."""
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def get_api_key():
    """Return an API key from the file."""
    with open(resource_path('./keys/api.txt')) as f:
        key = f.read()

    return key


def rebrickable_api(part_num):
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
            message_label.configure(text="API Error.")
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, requests.exceptions.JSONDecodeError):
        message_label.configure(text="Connection Error.")


def create_part_image(link):
    """Return tkinter image from URL, remove background and resize to 100x100 pixels."""
    u = urlopen(link)
    raw_data = u.read()
    u.close()
    # Create a PIL Image object from the raw data
    image = img.open(io.BytesIO(raw_data))
    # Manipulate image
    resized_image = image.resize((100, 100))
    final_image = remove(resized_image)
    # Create a PhotoImage object from the resized image
    photo = imgtk.PhotoImage(final_image)

    return photo


def update_window():
    """Update an application window."""

    global part_number_variable
    search_term = search_entry.get()
    load_catalog()

    if search_term:
        try:
            part_img_url, part_number, part_name, part_url = rebrickable_api(search_term)

            image = create_part_image(part_img_url)
            part_drawing_label.configure(image=image, bg=colors[1])
            part_drawing_label.image = image

            part_number_variable = StringVar(root, part_number)
            part_number_label.configure(textvariable=part_number_variable)
            part_name_label.configure(text=part_name)
            bricklink_button.configure(command=lambda: webbrowser.open(part_url))
            message_label.configure(text="")
            if search_term in catalog:
                box = catalog[search_term]
                box_label.configure(text=f"BOX: {box}")
            else:
                box_label.configure(text="NOT IN COLLECTION", fg=colors[0])
        except TypeError:
            message_label.configure(text="Wrong part number")
    else:
        message_label.configure(text="Please enter part number.")


def add_to_catalog():
    """Add lego part with the box number to the catalog."""
    part_number = part_number_variable.get()
    box_number = box_entry.get()
    if box_number and part_number != "Part number":
        if part_number not in catalog:
            catalog[part_number] = box_number.upper()
            box_label.configure(text=f"BOX: {catalog[part_number]}")
            save_catalog()
        else:
            message_label.configure(text="Item already exist in the collection.")
    else:
        message_label.configure(text="Enter box number or search for a part.")


def delete_from_catalog():
    """Delete lego part from the catalog."""
    part_number = part_number_variable.get()
    if part_number != "Part number":
        if messagebox.askyesno("Warning", message="Are you sure ?"):
            del catalog[part_number]
            box_label.configure(text="NOT IN COLLECTION", fg=colors[0])
            save_catalog()
        else:
            message_label.configure(text="No changes made.")
    else:
        message_label.configure(text="Nothing to delete.")


def save_catalog():
    """Save catalog to .json file."""
    with open('catalog.json', 'w') as file:
        json.dump(catalog, file)
    message_label.configure(text="Success. Catalog saved.")


def load_catalog():
    """Load catalog from .json file."""
    global catalog
    try:
        with open('catalog.json', 'r') as file:
            catalog = json.load(file)
    except FileNotFoundError:
        catalog = {}


# Create the window and widgets
root = Tk()
root.title("Brick Sorter")
root.resizable(False, False)
root.configure(bg=colors[1])
root.iconbitmap(resource_path("./images/BS.ico"))

# Use these fonts
font_reg = Font(file='font/Manrope-Regular.ttf', family='Manrope')
font_bold = Font(file='./font/Manrope-ExtraBold.ttf', family='Manrope ExtraBold')

# Set the window geometry and place the window in the center of the screen
window_width = 540
window_height = 400
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Calculate the x and y coordinates to center the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
# Set the window's position
root.geometry(f'{window_width}x{window_height}+{x}+{y}')


background_image = PhotoImage(file=resource_path('./images/background.png'))
background_label = Label(image=background_image,
                         borderwidth=0)
background_label.pack()

app_name = Label(text="BRICK SORTER",
                 font=('Manrope ExtraBold', 27),
                 bg=colors[1],
                 fg=colors[0])
app_name.place(x=140, y=0)

search_entry = Entry(justify='center',
                     font=('Manrope', 14, 'bold'),
                     bg=colors[0],
                     fg=colors[5],
                     borderwidth=0,
                     width=12)
search_entry.place(x=190, y=57, height=25)
search_entry.bind('<Return>', lambda event=None: search_button.invoke())
search_entry.focus()

search_button_image = PhotoImage(file=resource_path('./images/SEARCH_button.png'))
search_button = Button(image=search_button_image,
                       bg=colors[0],
                       activebackground=colors[0],
                       borderwidth=0,
                       command=update_window)
search_button.place(x=370, y=58)

part_drawing_image = PhotoImage(file=resource_path('./images/logo.png'))
part_drawing_label = Label(image=part_drawing_image,
                           borderwidth=0)
part_drawing_label.place(x=220, y=100)

part_number_variable = StringVar(root, "Part number")
part_number_label = Label(textvariable=part_number_variable,
                          justify='center',
                          font=('Manrope', 11, 'bold'),
                          bg=colors[1],
                          fg=colors[5])
part_number_label.place(x=21, y=210, width=500)

part_name_label = Label(text="Part name",
                        justify='center',
                        font=('Manrope', 11, 'bold'),
                        bg=colors[1],
                        fg=colors[5])
part_name_label.place(x=21, y=235, width=500)

bricklink_button = Button(text="Bricklink",
                          borderwidth=0,
                          font=('Manrope', 10, 'bold', 'underline'),
                          bg=colors[1],
                          fg=colors[5],
                          activebackground=colors[1],
                          activeforeground=colors[5])
bricklink_button.place(x=21, y=260, width=500)

box_label = Label(text="",
                  justify='center',
                  font=('Manrope ExtraBold', 13),
                  bg=colors[1],
                  fg=colors[0])
box_label.place(x=121, y=290, width=300)

box_entry = Entry(justify='center',
                  font=('Manrope', 12, 'bold'),
                  bg=colors[0],
                  fg=colors[5],
                  borderwidth=0,
                  width=4)
box_entry.place(x=158, y=329)

add_button_image = PhotoImage(file=resource_path('./images/ADD_button.png'))
add_button = Button(image=add_button_image, 
                    bg=colors[1], 
                    activebackground=colors[1], 
                    borderwidth=0,
                    command=add_to_catalog)
add_button.place(x=231, y=326)

delete_button_image = PhotoImage(file=resource_path('./images/DELETE_button.png'))
delete_button = Button(image=delete_button_image, 
                       bg=colors[1], 
                       activebackground=colors[1],
                       borderwidth=0,
                       command=delete_from_catalog)
delete_button.place(x=323, y=326)

message_label = Label(text="",
                      font=("Manrope", 10),
                      bg=colors[1], 
                      fg=colors[4])
message_label.place(x=10, y=374)

root.mainloop()
