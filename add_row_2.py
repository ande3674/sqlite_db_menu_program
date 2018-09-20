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

def add_row():
    print()
    print('Enter information for the product...')

    try:
        p_key = int(input("Enter the unique product key: "))
        p_name = input("Enter the product name: ")
        price = float(input("Enter the sale price for the product: "))
        p_desc = input("Enter the product description: ")
        num_in_stock = int(input("Enter the number of this product that are in stock: "))
        cost_to_make = float(input("Enter the cost to make this product: "))
        num_sold = int(input("Enter the number of this product sold so far: "))
        print()

        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()

        c.execute("INSERT INTO {tn} ({c1}, {c2}, {c3}, {c4}, {c5}, {c6}, {c7}) "
                  "VALUES ({v1}, {v2}, {v3}, {v4}, {v5}, {v6}, {v7})"
                  .format(tn=products_table, c1=id_field, c2=name_field, c3=price_field, c4=description_field,
                          c5=num_in_stock_field, c6=cost_to_make_field, c7=num_sold_field,
                          v1=p_key, v2='"' + p_name + '"', v3=price, v4='"' + p_desc + '"', v5=num_in_stock, v6=cost_to_make, v7=num_sold))

        conn.commit()
        conn.close()

        print('Row added successfully.')

    except ValueError:
        print("ERROR! Double check your input and try again...")
        print()

    print()