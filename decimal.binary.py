num=int(input("enter the number"))
b_n=0
i=0
while num!=0:
    rem=num%2
    a=pow(10,i)
    b_n=b_n+rem*a
    num=num/2
print(num)    
