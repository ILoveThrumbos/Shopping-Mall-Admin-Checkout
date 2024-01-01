class Transaction:
    def __init__(self, date, barcode, price):
        self.date = date
        self.barcode = barcode
        self.price = price



    def __str__(self):
        return f"{self.date} {self.price} {self.barcode}"


