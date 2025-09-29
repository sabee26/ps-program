class laptop:
    def __init__(self):
        self.processor =""
        self.ram=""
    def display(self):
        print("processor: ", self.processor)
        print("ram: ", self.ram)

hp=laptop()
hp.processor="i7"
hp.ram="8gb"

hp.display()
        

    