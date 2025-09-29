year=int(input("enter a value: "))

def is_leapyear():
    if(year%4==0):
        return True
    else:
        return False
a=is_leapyear()
print(a)
