"""
Code is prepared to help icecream seller to optimize the icecream sales.
It uses the past history to optimize the stock and determine the most
popular icecream. 
"""

import gspread
from google.oauth2.service_account import Credentials
from math import *           # Import the math library


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('ScoopsofLife')


def get_order_data():
    """
    Run a while loop to collect a valid string input of data from the user
    via the terminal. These numbers represent scoop of icecreams for the different flavors.
    Icecreams are normally measured in Kg to compare with the stock. 
    1 scoop is assumed to be 0.1 kg. 
    
    Realistic input values are from 200 to 500 scoops. 
    """
    while True:
        print("------------------------------------------------\n")
        print("Please enter order data from the last market.\n")
        print("Realistic data are from 100 to 500 scoops\n")
        print("------------------------------------------------\n")
        
        chocolate_str = input("Enter Chocolate Scoops:\n")
        vanilla_str = input("Enter Vanilla Scoops:\n")
        strawberry_str = input("Enter Strawberry Scoops:\n")
        mint_str = input("Enter Mint Scoops:\n")
        saffron_str = input("Enter Saffron Scoops:\n")

        ice_cream_order = [chocolate_str, vanilla_str, strawberry_str, mint_str, saffron_str]
        ice_cream_flavors = ["Chocolate", "Vanilla", "Strawberry", "Mint", "Saffron"]

        if validate_data(ice_cream_order):
            print("Data is valid!\n")
            break     

    order_data = []                                 # define the list which shows data in kg
    for scoop in ice_cream_order:
        scoop = float(scoop)*0.1                    # convert 1 scoop into 0.1 kg
        order_data.append(float(scoop))

    total_order = sum(order_data)
    #print(total_order)

    return order_data, ice_cream_flavors


def validate_data(values):
    """
    Inside the try, converts all string values into float.
    Raises ValueError if strings cannot be converted into float,
    Purpose is to raise an error even if any number is missing
    """
    try:
        
        for value in values:
            value = float(value)

        
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def find_favorit(order_data,flavors):
    """
    Purpose of this function is to identify the favorit icecream of the day. 
    """

    # gives the index of the most favorit icecream from the list
    popular_index = order_data.index(max(order_data)) 
    popular_flavor = flavors[popular_index]             # Provides the best flavor
    favorit_quantity = order_data[popular_index]        # provides quantity of the favorit icecream

    total_order = sum(order_data)
    favorit_contribution = (favorit_quantity/total_order)*100

    favorit_icecream = [popular_flavor, format(favorit_quantity, ".2f"), 
                        format(total_order, ".2f"), str(format(favorit_contribution, ".2f")) + " %"]


    return favorit_icecream



def update_worksheet(data, worksheet):
    """
    Receives a list of values to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")


def calculate_surplus_data(order_row):
    """
    Compare order with stock and calculate the surplus for each item type.

    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates orders, which were not fulfilled 
    """

    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    surplus_data = []
    for stock, order in zip(stock_row, order_row):
        surplus = float(stock) - order
        surplus_data.append(surplus)

    return surplus_data


def get_last_5_entries_order(n):
    """
    Collects columns of data from order worksheet, collecting
    the last 5 entries for each icecreams and returns the data
    as a list of lists.
    """
    order = SHEET.worksheet("order")

    columns = []
    for ind in range(1, n+1):
        column = order.col_values(ind)
        columns.append(column[-5:])

    return columns


def calculate_stock_data(data):
    """
    Calculate the average stock for each item type, adding 10%
    """
    print("Calculating stock data...\n")
    new_stock_data = []

    for column in data:
        int_column = [float(num) for num in column]
        average = sum(int_column) / len(int_column)
        stock_num = average * 1.1
        new_stock_data.append(round(stock_num))

    return new_stock_data


def main():
    """
    Run all program functions
    """

    # Enter data into terminal by user
    order_data,flavors = get_order_data()
    update_worksheet(order_data, "order")

    # Identifying the most popular flavor with the % contribution
    favorit_icecream =  find_favorit(order_data,flavors)
    update_worksheet(favorit_icecream, "favorit_flavor")
    
    # Calculate the surplus data
    new_surplus_data = calculate_surplus_data(order_data)
    update_worksheet(new_surplus_data, "icecream_surplus")

    # get last five entries in column form
    order_columns = get_last_5_entries_order(len(order_data))
    
    # calculation of stock data based on average of last 5 days entries
    stock_data = calculate_stock_data(order_columns)
    update_worksheet(stock_data, "stock")
   
print("Welcome to Scoops of Life Data Automation")
main()