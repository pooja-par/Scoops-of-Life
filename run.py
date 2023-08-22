"""
Code is prepared to help icecream seller to find optimize the icecream sales.
Shop has the following icecream flavors. 
1. vanila, 2. browncrunch, 3. saffron, 4. caramel apple 5. mocha macchiato
6. peanutbutter pie 7. dark chocolate 8. strawberry 9. lemon
"""
import gspread
from google.oauth2.service_account import Credentials
import math  # Import the math library


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('ScoopsofLife')


def get_sales_data():
    """
    Get sales figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 9 numbers separated
    by commas. These numbers represent scoop of icecreams for the different flavors.
    Icecreams are normally measured in Kg to compare with the stock. 1 scoop is assumed to be 0.1 kg. 
    Scoops are being converted in kg by multiplication of each scoop with 0.1. 
    """
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be nine numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60,70,80,90\n")
        print("In the sequence of:")
        print("vanila, browncrunch, saffron, caramel apple, mocha macchiato, peanutbutter pie, dark chocolate, strawberry, lemon\n")

        data_str = input("Enter your data here:\n")

        sales_data_scoop = data_str.split(",")
      
        
        if validate_data(sales_data_scoop):
            #sales_data = sales_data.*0.1         # convert scoop into kg
            print("Data is valid!")
            break     

    sales_data = []                                 # define the list which shows data in kg
    for scoop in sales_data_scoop:
        scoop = float(scoop)*0.1                    # convert 1 scoop into 0.1 kg
        sales_data.append(float(scoop))
    #print(sales_data)

    return sales_data


def validate_data(values):
    """
    Inside the try, converts all string values into float.
    Raises ValueError if strings cannot be converted into float,
    or if there aren't exactly 9 values.
    """
    try:
        for value in values:
            value = float(value)
         
        if len(values) != 9:
            raise ValueError(
                f" Exactly 9 values required, you provided {len(values)}"
            )

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")


def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.

    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock was sold out.
    """
    print("Calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    
    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)

    return surplus_data


def get_last_5_entries_sales():
    """
    Collects columns of data from sales worksheet, collecting
    the last 5 entries for each sandwich and returns the data
    as a list of lists.
    """
    sales = SHEET.worksheet("sales")

    columns = []
    for ind in range(1, 7):
        column = sales.col_values(ind)
        columns.append(column[-5:])

    return columns


def calculate_stock_data(data):
    """
    Calculate the average stock for each item type, adding 10%
    """
    print("Calculating stock data...\n")
    new_stock_data = []

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        stock_num = average * 1.1
        new_stock_data.append(round(stock_num))

    return new_stock_data

def ulate_scoops_from_kilograms(kilograms):
   
    scoops_per_kilogram = 1000 / 113  # 1kg = 1000/113 scoops
    scoops = kilograms * scoops_per_kilogram
    return scoops


def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    #sales_data = [float(num) for num in data]
    """
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, "surplus")
    sales_columns = get_last_5_entries_sales()
    stock_data = calculate_stock_data(sales_columns)
    update_worksheet(stock_data, "stock")
    """
    


print("Welcome to Scoops of Life Data Automation")
main()