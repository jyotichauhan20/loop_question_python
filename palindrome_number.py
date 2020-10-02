num=int(input("enter the number"))
pali=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if pali==rev:
    print("it is palindrome number")
else:
    print("it is not a palindrome number")        