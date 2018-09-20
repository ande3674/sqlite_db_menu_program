import sqlite3
import display_all_rows_5

sqlite_file = 'products.sqlite'
products_table = 'products'
id_field = 'id'
name_field = 'name'
price_field = 'price'
description_field = 'description'
num_in_stock_field = 'number_in_stock'
cost_to_make_field = 'cost_to_make'
num_sold_field = 'number_sold'


def display_one_row():

    # user picks what col they want to select
    display_column_selection_menu()
    print()

    try:
        selection = 0
        while selection < 1 or selection > 6:
            selection = int(input("Enter the column you want to select for by entering 1-6: "))

        # user enters col match information
        update_to = input("What is the selected for column supposed to match?: ")

        # select and display one row that matches the input
        # SELECT * FROM {tn} WHERE col_choice = user_input
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()

        # build the select statement based on what column the user would like to search
        if (selection == 1):
            sql_statement = "SELECT * FROM {tn} WHERE {cn} LIKE ".format(tn=products_table, cn=name_field)
        elif (selection == 2):
            sql_statement = "SELECT * FROM {tn} WHERE {cn} LIKE ".format(tn=products_table, cn=price_field)
        elif (selection == 3):
            sql_statement = "SELECT * FROM {tn} WHERE {cn} LIKE ".format(tn=products_table, cn=description_field)
        elif (selection == 4):
            sql_statement = "SELECT * FROM {tn} WHERE {cn} LIKE ".format(tn=products_table, cn=num_in_stock_field)
        elif (selection == 5):
            sql_statement = "SELECT * FROM {tn} WHERE {cn} LIKE ".format(tn=products_table, cn=cost_to_make_field)
        elif (selection == 6):
            sql_statement = "SELECT * FROM {tn} WHERE {cn} LIKE ".format(tn=products_table, cn=num_sold_field)

        # complete the sql statement ... if the variable is text we need to add quotations around it
        if (selection == 1 or selection == 3):
            sql_statement += '"' + update_to + '"'
        else:
            sql_statement += update_to

        # we also only want one result
        sql_statement += " LIMIT 1"
        c.execute(sql_statement)

        print()
        print('RESULTS')

        for row in c:

            print("ID: ", str(row[0]))
            print("NAME: ", row[1])
            print("PRICE: ", row[2])
            print("DESCRIPTION: ", row[3])
            print("NUMBER IN STOCK: ", row[4])
            print("COST TO MAKE: ", row[5])
            print("NUMBER SOLD: ", row[6])
            print()

        conn.commit()
        conn.close()

    except ValueError:
        print('There was an error selecting the row, please double check your data and try again.')

def display_column_selection_menu():

    print('1. name')
    print('2. price')
    print('3. description')
    print('4. number in stock')
    print('5. cost to make')
    print('6. number sold')
    print('')