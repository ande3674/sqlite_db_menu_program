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

def delete_row():

    print('Here is the table info: ')
    display_all_rows_5.display_rows()

    try:
        choice = int(input("Enter the ID of the row you wish to delete: "))

        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()

        c.execute("DELETE FROM {tn} WHERE {cn}={v}".format(tn=products_table, cn=id_field, v=choice))

        conn.commit()
        conn.close()

    except ValueError:
        print('There was an error deleting the row, please double check your data and try again.')