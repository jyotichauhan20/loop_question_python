num1=int(input("enter the number"))
num2=int(input("enter the number"))
lcm=1
i=1
while i>0:
    if i%num1==0 and i%num2==0:
        lcm=i
        break
    i=i+1
print(lcm)
