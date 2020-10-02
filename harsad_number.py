num=int(input("enter the number"))
n=num
rem=0
s=0
while n>0:
    rem=n%10
    s=s+rem
    n=n//10
if num%s==0:
    print(num,"it is harsad number")
else:
    print(num,"it is not a harsad number")        