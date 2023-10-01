import io
import json
import requests
from PIL import Image, ImageTk
from urllib.request import urlopen


def get_api_key():
    """Return an API key from the file."""
    with open("keys/api.txt") as key:
        return key.read()


def rebrickable_api(part_num):
    """Return lego part information from rebrickable.com API."""
    lego_data = requests.get(f"https://rebrickable.com/api/v3/lego/parts/{part_num}/?key={get_api_key()}").json()
    bricklink_id = lego_data["external_ids"]["BrickLink"][0]
    part_url = f"https://www.bricklink.com/v2/catalog/catalogitem.page?P={bricklink_id}#T=C"
    return lego_data["part_img_url"], lego_data["part_num"], lego_data["name"], part_url


def create_part_image(link):
    """Return tkinter image from URL, remove background and resize to 100x100 pixels."""
    url_image = urlopen(link)
    raw_data = url_image.read()
    url_image.close()
    image = Image.open(io.BytesIO(raw_data))
    resized_image = image.resize((100, 100))
    return ImageTk.PhotoImage(resized_image)


def read_lego_colors():
    with open("data/lego_colors.json", "r") as json_file:
        data_dict = json.load(json_file)
        return data_dict['lego_colors']
