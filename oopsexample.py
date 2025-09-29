class shape():
    def area(self):
       return 0 
class rectangle(shape):
    def area(self):
        l=4
        b=6
        print(l*b)

angle=rectangle()
angle.area()