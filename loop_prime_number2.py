a=int(input("enter the number"))
i=2
while i<=a-1:
    if a%i==0:
        print("not prime number")
        break
    i=i+1
else:
    print("prime number")        