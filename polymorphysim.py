class animal():
    def sound(self):
        print("Animal makes a sound")
class dog(animal):
    def sound(self):
        print("dog barkes")
class bird(animal):
    def sound(self):
        print("bird sings")
a1=bird()
a1.sound()