

def get_api_key():
    """Return an API key from the file."""
    with open("keys/api.txt") as f:
        key = f.read()
    return key
