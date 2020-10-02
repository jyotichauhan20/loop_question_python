num=int(input("enter the number"))
s=0
while num>0:
    a=num%10
    num=num//10
    s=s+a
print(s)    