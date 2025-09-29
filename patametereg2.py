class teacher:
    def __init__(self,n,r):
        self.name=n
        self.regno=r
    def display(self):
        print("name: ", self.name)
        print("regno: ", self.regno)   
t1=teacher("malar", "001")
t1.display()

t2=teacher("sabeena", "002")
t2.display()