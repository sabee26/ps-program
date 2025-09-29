a=[]
sum =0;
print("enter the 5 numbers");
for i in range(5):
    n=int(input("enter the value" +str(i+1) + " "));
    a.append(n);
print(a);

sum=0;
for i in a:
    sum = sum + i;
print(sum);  
