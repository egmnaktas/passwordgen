# passwordgen
This Python code generates random password.

Importing Required Modules:

from tkinter import *: This imports all the classes, functions, and constants from the tkinter module, allowing us to use them without specifying the module name.
from tkinter import messagebox: This imports the messagebox module from tkinter, which provides functions for displaying message boxes.

Importing Additional Modules:
from random import choice, randint, shuffle: This imports specific functions (choice, randint) and the shuffle function from the random module. These functions are used for generating random passwords.

Importing pyperclip:

import pyperclip: This imports the pyperclip module, which provides a cross-platform clipboard interface. It allows copying the generated password to the clipboard.

Importing json:

import json: This imports the json module, which provides functions for working with JSON data.

Password Generator Function:

The password_generator function generates a random password based on a combination of letters, numbers, and symbols. It retrieves the values entered in the password entry field and generates a new password based on those values. The generated password is then displayed in the password entry field and copied to the clipboard using pyperclip.copy().

Save Password Function:

The save function is triggered when the "Add" button is clicked. It retrieves the values entered in the website, email, and password entry fields. It checks if the website and password fields are empty and displays an error message if they are. If not empty, it tries to open the data.json file for reading. If the file doesn't exist, it creates an empty dictionary data. The new data (website, email, and password) is added to the data dictionary. The data dictionary is then written back to the data.json file, overwriting the existing data if any. Finally, the website and password entry fields are cleared.

Find Password Function:

The find_password function is triggered when the "Search" button is clicked. It retrieves the value entered in the website entry field and tries to open the data.json file. If the file exists, it loads the JSON data into the data variable. It checks if the website exists in the data dictionary. If it does, it retrieves the email and password associated with the website and displays them in a message box. If the website doesn't exist, it displays an error message. If the data.json file doesn't exist, it displays an error message.

UI Setup:

The code sets up the graphical user interface (GUI) using the tkinter library.
It creates a main window with the title "Password Manager" and sets the padding and background color.
It creates a canvas to display the logo image.
It creates labels and entry fields for website, email/username, and password.
It creates buttons for generating passwords, saving passwords, and searching for passwords.
The mainloop() function is called to start the GUI event loop and keep the window displayed.

Note: Please make sure you have the logo image file (logo.png) in the same directory as the script for the logo to be displayed correctly.
