import hashlib
import sys


from product import Product
from superMarketDAO import SuperMarketDao


"""
*CHANGES*
Added login and menu
Added a basic flow of LOGIN > MENU > SUPERMARKET CHECKOUT (if option 7 is selected).
Login and menu is the admin system which includes a login and menu which allows the supermarket checkout
to be run.
Added str to the price float when finding barcode (converts to string)
"""


def login():
    credentials = "useradmin_Password@1"  # user name = "useradmin" and password = "Password@1"

    with open("login.bin", "wb") as file:
        file.write(hashlib.sha512(credentials.encode('utf-8')).digest())
        file.close()

    with open('login.bin', 'rb') as file:
        user_name = input("enter un: ")
        pw = input("enter pw: ")
        user_cred = "".join([user_name, '_', pw])
        # print(user_cred)
        user_cred = hashlib.sha512(user_cred.encode('utf-8')).digest()  # create hash
        if user_cred == file.read():  # verify hash (password)
            print("OK")
            print('\n--------Welcome to the Admin System Menu.--------\n')
            return menu()
        else:
            print("Error! Incorrect credentials!")
            return login()


# Admin Menu
def menu():

    dao = SuperMarketDao('product_db.db')
    while True:
        # Starting program
        print("[a] Option a: Add Product")
        print("[b] Option b: List all Products")
        print("[c] Option c: Find Product")
        print("[d] Option d: List all Transactions")
        print("[e] Option e: Display BarChart of Products Sold by Quantity")
        print("[f] Option f: Display Excel Document of Transaction Reports")
        print("[g] Option g: Exit")
        choice = input("Enter your option: ")
        while choice not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
            print("Invalid option")
            choice = input("Enter your option: ")
        if choice == 'a':
            try:
                print(dao.addProduct())
            except Exception:
                print("Invalid input. Please try again.")
                continue

        elif choice == 'b':
            try:
                print(dao.listAllProducts())
            except Exception:
                print("Invalid input. Please try again.")
                continue
        elif choice == 'c':
            try:
                barcode = input('Barcode:')
                print(dao.findProduct(Product(barcode, '', '', '')))
            except Exception:
                print("Invalid input. Please try again.")
                continue
        elif choice == 'd':
            try:
                print(dao.listAllTransactions())
            except Exception:
                print("Invalid input. Please try again.")
                continue
        elif choice == 'e':
            try:
                print(dao.displayBarchartOfProductsSold())
            except Exception:
                print("Invalid input. Please try again.")
                continue
        elif choice == 'f':
            try:
                print(dao.displayExcelReportOfTransactions())
            except Exception:
                print("Invalid input. Please try again.")
                continue
        elif choice == 'g':
            print("Exist Success!")
            sys.exit()
        else:
            print("Invalid option. Please try again.")
            continue


def main():
    print('\n--------Welcome to the Login Screen.--------\n')
    try:
        login()
        menu()
    except Exception as e:
        print("An error occurred:", str(e))


main()

