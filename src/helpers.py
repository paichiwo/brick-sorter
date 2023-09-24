import requests


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
