num=int(input("enter the number"))
i=1

s=0
while i<=num:
    if num%i==0:
        per=i
        s=s+per
    i=i+1
if s==num:
    print(num,"it is perfect number")
else:
    print(num,"it is not perfect number")