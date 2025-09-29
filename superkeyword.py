class a():
    def __init__(self):
        print("A")

        def display(self):
            print("your in class a")

class b():
    def __init__(self):
      super() .__init__() 
      print("B")
    
    def display(self):
            print("your in class a")

class c(b,a):
    def __init__(self):
      super() .__init__() 
      print("c")
    
    def display(self):
            print("your in class c")

obj=c()


    