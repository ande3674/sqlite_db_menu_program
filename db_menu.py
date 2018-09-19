import sqlite3
import create_db_table_1
import add_row_2
import update_row_3
import delete_row_4
import display_all_rows_5
import display_one_row_6

### DATABASE MENU PROGRAM ###

# Program constants
CREATE_DB_AND_TABLE_CHOICE = 1
ADD_ROW_CHOICE = 2
UPDATE_ROW_CHOICE = 3
DELETE_ROW_CHOICE = 4
DISPLAY_ALL_ROWS_CHOICE = 5
DISPLAY_SINGLE_ROW_CHOICE = 6
QUIT_CHOICE = 7


def main():
    choice = 0

    while choice != QUIT_CHOICE:
        # display menu
        display_menu()

        try:
            # get user choice
            choice = int(input('Enter your choice: '))
            print('')

        except ValueError:
            print('ERROR: You must enter a number.')
            print('')

        if choice == CREATE_DB_AND_TABLE_CHOICE:
            print('Creating products database and table...')
            print('')
            create_db_table_1.create_db_and_table()

        elif choice == ADD_ROW_CHOICE:
            add_row_2.add_row()
            # conn = sqlite3.connect('products.sqlite')
            # c = conn.cursor()
            # c.execute("SELECT * FROM {tn}".format(tn='products'))
            # for row in c:
            #     print("PRODUCT KEY:", row[0])
            #     print('PRODUCT NAME:', str(row[1]))
            #     print('PRODUCT PRICE:', str(row[2]))
            # conn.commit()
            # conn.close()


        elif choice == UPDATE_ROW_CHOICE:
            update_row_3.update_row()
            # conn = sqlite3.connect('products.sqlite')
            # c = conn.cursor()
            # c.execute("SELECT * FROM {tn}".format(tn='products'))
            # for row in c:
            #     print("PRODUCT KEY:", row[0])
            #     print('PRODUCT NAME:', str(row[1]))
            #     print('PRODUCT PRICE:', str(row[2]))
            # conn.commit()
            # conn.close()

        elif choice == DELETE_ROW_CHOICE:
            break

        elif choice == DISPLAY_ALL_ROWS_CHOICE:
            display_all_rows_5.display_rows()

        elif choice == DISPLAY_SINGLE_ROW_CHOICE:
            break

        else:
            choice = int(input('Invalid menu number. Select a menu option by entering the menu number: '))
            print('')

    print('Thanks for using the products database program')


# display menu function
def display_menu():
    print('***** DATABASE MENU OPTIONS *****')
    print('1. Create database and database table')
    print('2. Add a row of data to the table')
    print('3. Update a row in the table')
    print('4. Delete a row of data from the table')
    print('5. Display all rows in the table')
    print('6. Display a row of data based on an input value')
    print('7. Quit program')
    print('**********************************')
    print()


main()