import sqlite3

sqlite_file = 'products.sqlite'
products_table = 'products'

def display_rows():

    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute("SELECT * FROM {tn}".format(tn=products_table))

    print()
    print("********************")
    print("*** ALL PRODUCTS ***")
    print("********************")

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