import sqlite3

# db and table info
sqlite_file = 'products.sqlite'
products_table = 'products'

# column info
# 1. id - PRIMARY KEY
id_field = 'id'
id_field_type = 'INTEGER'
# 2. product name - NOT NULL
name_field = 'name'
name_field_type = 'TEXT'
name_default = ''
# 3. product sale price - NOT NULL
price_field = 'price'
price_field_type = 'REAL'
price_default = 0.0
# 4. product description
description_field = 'description'
description_field_type = 'TEXT'
# 5. amount in stock
num_in_stock_field = 'number_in_stock'
num_in_stock_field_type = 'INTEGER'
# 6. cost to make
cost_to_make_field = 'cost_to_make'
cost_to_make_field_type = 'REAL'
# 7. amount sold
num_sold_field = 'number_sold'
num_sold_field_type = 'INTEGER'

def create_db_and_table():
    # Create the database ...
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('DROP TABLE {tn}'.format(tn=products_table))

    # Create the table and add columns
    c.execute('CREATE TABLE IF NOT EXISTS {tn} ({fn1} {ft1} PRIMARY KEY)'.format(tn=products_table, fn1=id_field, ft1=id_field_type))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} DEFAULT '{df}'".format(tn=products_table, cn=name_field, ct=name_field_type, df=name_default))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} DEFAULT '{df}'".format(tn=products_table, cn=price_field, ct=price_field_type, df=price_default))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=products_table, cn= description_field, ct=description_field_type))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=products_table, cn=num_in_stock_field, ct=num_in_stock_field_type))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=products_table, cn=cost_to_make_field, ct=cost_to_make_field_type))
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=products_table, cn=num_sold_field, ct=num_sold_field_type))

    c.execute("INSERT INTO {tn} ({c1}, {c2}, {c3}, {c4}, {c5}, {c6}, {c7}) VALUES (0, 't-shirt', 25.50, 'red t-shirt', 12, 3.50, 4)".format(tn=products_table, c1=id_field, c2=name_field, c3=price_field, c4=description_field, c5=num_in_stock_field, c6=cost_to_make_field, c7=num_sold_field))

    #c.execute("SELECT * FROM {}".format(products_table))
    #for row in c:
        #print(row[0])
        #print(row[1])

    # commit and close connection
    conn.commit()
    conn.close()