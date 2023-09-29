import io
import requests
from rembg import remove
from PIL import Image, ImageTk
from urllib.request import urlopen


def get_api_key():
    """Return an API key from the file."""
    with open("keys/api.txt") as f:
        key = f.read()
    return key


def rebrickable_api(part_num):
    """Return lego part information from rebrickable.com API."""
    key = get_api_key()
    url = f"https://rebrickable.com/api/v3/lego/parts/{part_num}/?key={key}"
    lego_data = requests.get(url).json()
    part_img_url = lego_data["part_img_url"]
    part_number = lego_data["part_num"]
    part_name = lego_data["name"]
    bricklink_id = lego_data["external_ids"]["BrickLink"][0]
    part_url = f"https://www.bricklink.com/v2/catalog/catalogitem.page?P={bricklink_id}#T=C"
    return part_img_url, part_number, part_name, part_url


def create_part_image(link):
    """Return tkinter image from URL, remove background and resize to 100x100 pixels."""
    url_image = urlopen(link)
    raw_data = url_image.read()
    url_image.close()
    image = Image.open(io.BytesIO(raw_data))
    resized_image = image.resize((100, 100))
    final_image = remove(resized_image)
    photo = ImageTk.PhotoImage(final_image)
    return photo


lego_colors = ['Aqua', 'Black', 'Blue', 'Blue-Violet', 'Bright Green', 'Bright Light Blue', 'Bright Light Orange', 'Bright Light Yellow', 'Bright Pink', 'Brown', 'Chrome Antique Brass', 'Chrome Black', 'Chrome Blue', 'Chrome Gold', 'Chrome Green', 'Chrome Pink', 'Chrome Silver', 'Copper', 'Coral', 'Dark Azure', 'Dark Blue', 'Dark Blue-Violet', 'Dark Bluish Gray', 'Dark Brown', 'Dark Gray', 'Dark Green', 'Dark Nougat', 'Dark Orange', 'Dark Pink', 'Dark Purple', 'Dark Red', 'Dark Salmon', 'Dark Tan', 'Dark Turquoise', 'Dark Yellow', 'Earth Orange', 'Flat Dark Gold', 'Flat Silver', 'Glitter Trans-Clear', 'Glitter Trans-Dark Pink', 'Glitter Trans-Light Blue', 'Glitter Trans-Neon Green', 'Glitter Trans-Orange', 'Glitter Trans-Purple', 'Glow In Dark Opaque', 'Glow In Dark Trans', 'Glow in Dark White', 'Green', 'Lavender', 'Light Aqua', 'Light Blue', 'Light Bluish Gray', 'Light Brown', 'Light Gray', 'Light Green', 'Light Lime', 'Light Nougat', 'Light Orange', 'Light Pink', 'Light Purple', 'Light Salmon', 'Light Turquoise', 'Light Violet', 'Light Yellow', 'Lilac', 'Lime', 'Maersk Blue', 'Magenta', 'Medium Azure', 'Medium Blue', 'Medium Brown', 'Medium Dark Pink', 'Medium Green', 'Medium Lavender', 'Medium Lime', 'Medium Nougat', 'Medium Orange', 'Medium Tan', 'Medium Violet', 'Metallic Black', 'Metallic Copper', 'Metallic Gold', 'Metallic Green', 'Metallic Silver', 'Milky White', 'Neon Yellow', 'Nougat', 'Olive Green', 'Orange', 'Pearl Dark Gray', 'Pearl Gold', 'Pearl Light Gold', 'Pearl Light Gray', 'Pearl Sand Blue', 'Pearl Very Light Gray', 'Pearl White', 'Pink', 'Purple', 'Red', 'Reddish Brown', 'Reddish Copper', 'Reddish Gold', 'Rust', 'Salmon', 'Sand Blue', 'Sand Green', 'Sand Purple', 'Sand Red', 'Satin Trans-Dark Blue', 'Satin Trans-Dark Pink', 'Satin Trans-Green', 'Satin Trans-Light Blue', 'Satin Trans-Purple', 'Satin Transparent Black', 'Satin White', 'Sky Blue', 'Speckle Black-Copper', 'Speckle Black-Gold', 'Speckle Black-Silver', 'Speckle DBGray-Silver', 'Tan', 'Trans-Black (2023)', 'Trans-Bright Green', 'Trans-Brown (Old Trans-Black)', 'Trans-Clear', 'Trans-Dark Blue', 'Trans-Dark Pink', 'Trans-Green', 'Trans-Light Blue', 'Trans-Light Bright Green', 'Trans-Light Green', 'Trans-Light Orange', 'Trans-Light Purple', 'Trans-Medium Blue', 'Trans-Neon Green', 'Trans-Neon Orange', 'Trans-Neon Yellow', 'Trans-Orange', 'Trans-Pink', 'Trans-Purple', 'Trans-Red', 'Trans-Very Lt Blue', 'Trans-Yellow', 'Very Light Bluish Gray', 'Very Light Gray', 'Very Light Orange', 'Violet', 'White', 'Yellow', 'Yellowish Green']
