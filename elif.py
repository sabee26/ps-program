salary=int(input("enter your salary: "))
age=int(input("enter your age: "))
if(salary>=20000 or age<=25):
    loanamount=int(input("required loan ammount: "))
    if(loanamount>50000):
      print("maximum loan amount is 50000")
    else:
      print("you are eligile")
else:
    print("you are not eligible")

  

