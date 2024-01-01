class Product:
    def __init__(self, barcode, name='', desc='', price=0.0):
        self.barcode = barcode
        self.name = name
        self.desc = desc
        self.price = price

    """
    *CHANGES*
    SuperMarketDao class was imported from the superMarketDAO.py.
    read_barcode method was modified to use the findProduct from the SuperMarketDao class to find the barcode.
    Now uses the database product_db.db table product as the binary file to read from instead of a .txt file.
    Added condition if barcode input is null return an error
    Added str to the price float when finding barcode (converts to string)
    """


    def get_barcode(self):
        return self.barcode

    def get_desc(self):
        return self.desc

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    def __str__(self):
        return f"{self.barcode} {self.name} {self.desc}  {str(self.price)}"
