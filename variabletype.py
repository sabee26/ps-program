class phone:
    chargertype = "c-type"  # class variable (shared)

    def __init__(self, brand,price):
        self.brand = brand
        self.price = price   # instance variable

    def display(self):
        print("brand", self.brand)
        print("price", self.price)
        print("chargertype", self.chargertype)

android = phone("sumsung","40,000")
iphone = phone("14promax","90,000")

android.display()
iphone.display()
