import sqlite3

sqlite_file = 'products.sqlite'
products_table = 'products'

id_field = 'id'
name_field = 'name'
price_field = 'price'
description_field = 'description'
num_in_stock_field = 'number_in_stock'
cost_to_make_field = 'cost_to_make'
num_sold_field = 'number_sold'

def update_row():
    # select row to update
    id_value = int(input("Enter the product id of the product you would like to update: "))

    # select column to update
    print('Please select which column you want to update: ')
    display_column_selection_menu()
    print()
    update_choice = 0
    while (update_choice < 1 or update_choice > 6):
        update_choice = int(input("Column number: "))

    # get the new column value
    if (update_choice == 1 or update_choice == 3):
        update_value = input('Enter the new value: ')
        update_value += '"'
    else:
        update_value = int(input('Enter the new value: '))

    # build sql statement
    #UPDATE products SET {cn}=col_val WHERE id=id_val
    sql_statement = "UPDATE products SET "

    if (update_choice == 1):
        sql_statement += 'name = "'
    elif (update_choice == 2):
        sql_statement += "price = "
    elif (update_choice == 3):
        sql_statement += 'description = "'
    elif (update_choice == 4):
        sql_statement += "number_in_stock = "
    elif (update_choice == 5):
        sql_statement += "cost_to_make = "
    else: # (update_choice == 6):
        sql_statement += "number_sold = "

    sql_statement += str(update_value)
    sql_statement += " WHERE id="
    sql_statement += str(id_value)

    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute(sql_statement)

    print("Updated product number", str(id_value), "successfully.")
    print()

    conn.commit()
    conn.close()

def display_column_selection_menu():

    print('1. name')
    print('2. price')
    print('3. description')
    print('4. number in stock')
    print('5. cost to make')
    print('6. number sold')
    print('')