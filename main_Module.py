import sys
from checkOutRegister import CheckoutRegister


def scan_product(register):
    """
    Method used to scan a product via accepting the barcode from the user
    and adding it to the register.

    :param register: The CheckoutRegister object.
    """
    product_barcode = input('\nPlease enter the barcode of your item: ')
    register.scan_item(product_barcode)


def continue_exit():
    """
    Prompts user a choice to continue as c or exit with e. Both are .lower so not case-sensitive.

    If continue chosen, a new instance of the CheckoutRegister will be created (assigned by register).
    Furthermore, the the products list (products[]) attributed to the register object will be cleared.
    If exit is chosen, it will  close the system with the sys.exit(0) and exit the program.

    :return: True if the user chooses to continue, False if the user chooses to exit.


    """
    while True:
        choice = input("Would you like to continue(C) or exit(E) the program?: ")
        if choice.lower() == 'c':
            register = CheckoutRegister()
            register.products.clear()
            return main()
        elif choice.lower() == 'e':
            print("Exiting the system...")
            sys.exit(0)
        else:
            print("Invalid input. Please enter 'C' or 'E'.")
    #return false


def main():
    """
    The main function executing the supermarket checkout program.
    :return:
    """
    print('\n--------Welcome to the Supermarket Checkout.--------\n')
    register = CheckoutRegister()
    scan_product(register)
    accept_payment = register.calculate_payment_due()
    balance = register.payment(accept_payment)
    register.print_receipt(balance)
    register.save_transaction(register.products)
    continue_exit()


main()

