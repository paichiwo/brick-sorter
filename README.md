## **Brick Sorter**

![](img/screenshot/screenshot_1.png)

This is a desktop application called Brick Sorter that allows you to search for LEGO parts and manage your LEGO collection. The app uses the Rebrickable.com API to fetch information about LEGO parts based on their part numbers. It also provides features to add parts to your collection and associate them with box numbers.

## **Installation**

To run the Brick Sorter app, please follow these steps:   

Make sure you have Python installed on your system (version 3.7 or higher).  
Clone the repository or download the source code files.   
Install the required Python packages by running the following command:

`pip install rembg Pillow tk tkextrafont` or `pip install -r requirements.txt`

Create **api.txt** with your own Rebrickable.com API key and place it in the **key** folder in the root directory. If you don't have an API key, you can obtain one by signing up on the Rebrickable.com website.

Run the following command to start the application:

`python brick_sorter.py`

## **Features**

The Brick Sorter app provides the following features:

*   **Search**: Enter a LEGO part number in the search field and press Enter or click the Search button. The app will fetch information about the part from the Rebrickable.com API and display the part's image, number, name, and a link to its page on BrickLink.
*   **Add to Catalog**: After searching for a part, you can enter a box number in the box entry field and click the Add button to add the part to your catalog. The catalog associates each part number with a box number.
*   **Delete from Catalog**: To remove a part from your catalog, select the part by searching for its part number, and then click the Delete button. A confirmation prompt will appear before deleting the part.

## **Usage**

1.  Launch the Brick Sorter app.
2.  Enter a LEGO part number in the search field and press Enter or click the Search button.
3.  The app will display the part's image, number, name, and a link to its page on BrickLink.
4.  If the part is already in your catalog, the associated box number will be displayed. Otherwise, it will show "NOT IN COLLECTION" in red.
5.  To add the part to your catalog, enter a box number in the box entry field and click the Add button.
6.  To delete a part from your catalog, search for the part, and then click the Delete button. Confirm the deletion in the prompt.
7.  The app will automatically save your catalog whenever you add or delete a part.

Note: The catalog file (**catalog.json**) is stored in the same directory as the application.

## **Dependencies**

The Brick Sorter app relies on the following Python packages:

*   **rembg**: A Python library for removing image backgrounds.
*   **Pillow**: A fork of the Python Imaging Library (PIL) for image processing.
*   **tkinter**: The standard Python interface to the Tk GUI toolkit.
*   **tkextrafont**: A library for using additional fonts in Tkinter applications.

These packages will be automatically installed when you follow the installation instructions mentioned above.

## **License**

This project is licensed under the [MIT License](./LICENSE).