# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# ABryant,6.5.2020, Updated Product class with a constructor, added data descriptions
# ABryant,6.6.2020, Updated FileProcessor and IO Classes with new methods and docstrings
# ABryant,6.7.2020, Added remove_products method to IO class and cleaned up formatting for presentation
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #

strFileName = 'products.txt'  # A string that holds the relevant filename
menu_option = ''  # A string that holds the user's menu choice
lstOfProductObjects = []  # A list that holds the Product objects while program is running


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's name
        product_price: (float) with the products's standard price
    methods:
        __init__(self, product_name, product_price): a constructor method to create Product objects
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        ABryant,6.5.2020, Added constructor to Product Class
    """
    pass

    # TODO: Add Code to the Product class
    # --Constructor --
    def __init__(self, product_name, product_price):
        self.str_product_name = product_name
        self.str_product_price = product_price


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        read_data_from_file(file_name): -> (a list of product objects)
            Parameters supplied are a file name to read. The contents of the file are returned as a list.

        save_data_to_file(file_name, list_of_product_objects):
            Parameters supplied are the active file name and the active list of products. Nothing is returned.

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        ABryant,6.6.2020,Created FileProcessor Methods and Updated Docstring
    """
    pass

    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name):
        temp_list_of_products = []
        active_file = open(file_name, "r")
        for row in active_file:
            row = row.strip('\n')
            temp_list_of_products.append(row)
        active_file.close()
        return temp_list_of_products

    # TODO: Add Code to process data to a file
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        active_file = open(file_name, 'w')
        for row in list_of_product_objects:
            active_file.write(str(row) + '\n')
        active_file.close()
        print('Products have been saved.')
        return


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """Receives inputs and presents outputs to manage a product list.

    methods:
        menu_options(): Receives no parameters, presents menu options.

        menu_input(): Receives no parameters, requests a menu choice.

        review_products(): Receives no parameters, presents any existing products.

        add_products(): Receives no parameters, creates a new Product object from user inputs, adds to product list.

    changelog: (When,Who,What)
        ABryant,6.6.2020,Created IO Methods and Updated Docstring
    """
    pass

    # TODO: Add code to show menu to user
    @staticmethod
    def menu_options():
        print('\nMenu options: \n 1 - Review product list\n 2 - Add product\n 3 - Remove product\n 4 - Save and quit')
        return

    # TODO: Add code to get user's choice
    @staticmethod
    def menu_input():
        temp_menu_choice = int(input('Please select a menu option: '))
        return temp_menu_choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def review_products():
        if len(lstOfProductObjects) == 0:
            print('No products have been added yet.')
        else:
            for row in lstOfProductObjects:
                print(row)
        return

    # TODO: Add code to get product data from user
    @staticmethod
    def add_products():
        name_input = str(input('Please enter product name: ')).lower()
        price_input = float(input('Please enter product price: '))
        new_product = Product(name_input, price_input)
        lstOfProductObjects.append((new_product.str_product_name + ', $' + str(new_product.str_product_price)))
        print('Product has been added.')
        return

    @staticmethod
    def remove_products():
        product_to_remove = str(input('Enter the product name to be removed: ')).lower()
        row_counter = 0
        for row in lstOfProductObjects:
            if product_to_remove in row.split(','):
                lstOfProductObjects.remove(row)
                print('"' + product_to_remove + '" has been removed.')
                row_counter += 1
            elif row_counter > 0:
                break
        if row_counter == 0:
            print('"' + product_to_remove + '" not found in product list.')

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body

# Load data from file into a list of product objects when script starts


list_file = open(strFileName, 'a')
list_file.close()
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)


# Show user a menu of options
while True:
    IO.menu_options()

    # Get user's menu option choice
    try:
        menu_choice = IO.menu_input()
    except ValueError as e:
        print('**Invalid Entry**\nPlease select a valid menu option.')
        menu_choice = ''

    # Show user current data in the list of product objects
    if menu_choice == int(1):
        IO.review_products()

    # Let user add data to the list of product objects
    elif menu_choice == int(2):
        try:
            IO.add_products()
        except ValueError as e:
            print('\n**Invalid Entry**\nProduct names must be alphanumeric.\nProduct prices must be numeric.')
            print('Neither field may be empty.')

    # extra: let the user remove products
    elif menu_choice == int(3):
        IO.remove_products()

    # let user save current data to file and exit program
    elif menu_choice == int(4):
        confirm_save = str(input('Ready to save and quit? Y/N: ')).upper()
        if confirm_save == 'Y':
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            break
        elif confirm_save == 'N':
            print('Products have not been saved.\nReturning to menu.')
        else:
            print('**Invalid Selection**\nProducts have not been saved.\nReturning to menu.')

    else:
        print('**Invalid Entry**\nPlease select a valid menu option.')

# Main Body of Script  ---------------------------------------------------- #
