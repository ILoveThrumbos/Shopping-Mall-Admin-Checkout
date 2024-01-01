import sqlite3

try:

    db = sqlite3.connect('product_db.db')
    cursor = db.cursor()
    query = ('''CREATE TABLE IF NOT EXISTS product (
                            barcode CHAR(3) NOT NULL, name CHAR(25) NOT NULL, desc CHAR(50) NOT NULL, 
                            price FLOAT NOT NULL);''')
    cursor.execute(query)
    product = [('123', 'Bread', '500g', 2.5),
                       ('456', 'Milk', '1L', 2.5),
                       ('789', 'Sugar', '500g', 1.5),
                       ('101', 'Chocolate', '400g', 4.5),
                       ('988', 'Beans', '500g', 1.0),
                       ('866', 'Honey', '500g', 3.5),
            ('432', 'Skim Milk', '2L', 3.5),
            ('634', 'Brown Sugar', '1KG', 2.5),
            ('854', 'White Chocolate', '1KG', 4.5),
            ('104', 'Kidney Beans', '800g', 1.5)]
    query = "INSERT INTO product (barcode, name, desc, price) VALUES (?,?,?,?)"
    cursor.executemany(query, product)
    print('product table created successfully')
    cursor = db.cursor()
    query = '''DROP TABLE IF EXISTS transactions'''
    query = ('''CREATE TABLE IF NOT EXISTS transactions ( date CHAR(10) NOT NULL, barcode CHAR(3) NOT NULL, 
    price FLOAT NOT NULL);''')
    cursor.execute(query)
    transactions = [('2022-11-12', '456', 3.5),
                    ('2022-11-13', '123', 2.5),
                    ('2022-11-14', '101', 4.5),
                    ('2022-11-15', '123', 2.5),
                    ('2022-11-16', '634', 2.5),
                    ('2022-11-17', '432', 3.5),
                    ('2022-11-18', '789', 1.5),
                    ('2022-11-19', '789', 1.5),
                    ('2022-11-20', '104', 1.5),
                    ('2022-11-21', '854', 4.5)]
    query = "INSERT INTO transactions (date, barcode, price) VALUES (?,?,?)"
    cursor.executemany(query,  transactions)
    print('transactions table created successfully')
    db.commit()
except Exception as e:
    print("Unable to display data. {}".format(e))

    db.rollback()
    raise e
finally:
    db.close()