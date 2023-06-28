import json
import requests

lego_part_information = []


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


def add_box_number(part_num, box_num):

    part_info_list = [rebrickable_api(part_num), box_num]
    return part_info_list


print(add_box_number("3022", "A"))





