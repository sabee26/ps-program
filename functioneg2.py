s_username="sabee";
s_password="143";
username=input("enter the username: ");
password=input("enter the password: ");

def validate():
    if(s_username==username and s_password==password):
        return True
    else:
        return False

a=validate()
print(a)
