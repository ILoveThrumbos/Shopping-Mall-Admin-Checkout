<h1 align="center">Shopping Mall Cart with Admin Checkout</h1>

## Introduction
Python checkout/shopping system that records transactions.

Includes a simple Python Unit Tests for Shopping Mall Cart. 

## Project Overview

The Java Bookstore implements a robust MVC structure:

- **Checkout System:** Reads product.txt barcodes, and prints the transactions into the transactin.txt when a transaction is completed.
  
- **Database Storage:**Uses sqllite3 to store and create database. 

- **Admin System:** Allow modification of products and transactions (add, list, find product and transactions. Also, displays excel files of BarChart of product sold and transaction report ).

## Diagram 

<!--Insert Diagram or GIF here (if applicable) to provide a visual representation of the MVC architecture and the flow of data in the Java Bookstore. !-->
Admin System Menu Options (Admin):

![image](https://github.com/ILoveThrumbos/Shopping-Mall-Admin-Checkout/assets/139453924/68a1f414-2ced-438c-bbeb-3ccd494187b7)

SuperMarket Checkout (User):

![image](https://github.com/ILoveThrumbos/Shopping-Mall-Admin-Checkout/assets/139453924/738afb0e-6740-467d-82d5-bb487dc5fb2a)


## Installation and Usage Instructions

### Prerequisites

Before getting started, ensure you have the following installed:

- [Python 3.10](https://www.python.org/downloads/)
- [PyCharms 2022-2023(Community edition works)](https://www.jetbrains.com/pycharm/download/?section=windows) 



### Steps to Run the Project

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ILoveThrumbos/Shopping-Mall-Cart-Python-Tests.git
2. Launch PyCharms.
   Choose "Open Project" and select the cloned shopping mall cart project.
3. Select a python interpreter.
4.  (OPTIONAL) If you wish to create own database/users, delete both db's (login_db.db & product_db.db).
5.  (If completing OPTIONAL step 4) Use the logindatabase.py and databases.py file templates to create user and database. 
6. To Run user checkout system type 'py test_checkOutRegister.py' in terminal.
7. To run Admin System Menu type 'py mainDAO.py' in terminal (Crendetials provided in mainDAO.py under login method).

### Known Issues
   - Non currently known.
   - 

## Support and Contributions
If you encounter any issues or have suggestions for improvement, please create an issue on the GitHub repository. Contributions are welcome, so feel free to submit pull requests to enhance the functionality or fix bugs.

Thank you for using the Java Bookstore! Happy reading!
