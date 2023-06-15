import json


# Dictionary to store the brick numbers and their corresponding boxes
catalog = {}


# Function to add a brick number and its box to the catalog
def add_to_catalog(brick_number, box):
    catalog[brick_number] = box


# Function to save the catalog to a JSON file
def save_catalog():
    with open('catalog.json', 'w') as file:
        json.dump(catalog, file)


# Function to load an existing catalog from a JSON file
def load_catalog():
    global catalog
    try:
        with open('catalog.json', 'r') as file:
            catalog = json.load(file)
    except FileNotFoundError:
        catalog = {}


# Function to search for a brick number in the catalog
def search_catalog(brick_number):
    if brick_number in catalog:
        return catalog[brick_number]
    else:
        return None


# Load an existing catalog (if available) when the app starts
load_catalog()

# Main program loop
while True:
    print("LEGO Sorting App")
    print("1. Add a brick number to the catalog")
    print("2. Search for a brick number")
    print("3. Save and exit")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        brick_number = input("Enter the brick number: ")
        box = input("Enter the storage box: ")
        add_to_catalog(brick_number, box)
        print("Brick added to the catalog.")

    elif choice == '2':
        brick_number = input("Enter the brick number to search: ")
        box = search_catalog(brick_number)
        if box:
            print(f"The brick with number {brick_number} is in box {box}.")
        else:
            print(f"The brick with number {brick_number} is not found in the catalog.")

    elif choice == '3':
        save_catalog()
        print("Catalog saved. Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
