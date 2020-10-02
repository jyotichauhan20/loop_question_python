num=(input("enter the number"))
order=len(str(num))
sum=0
a=num

while a>0:
    digit=a%10
    sum=sum+digit**order
    a=a//10
    
if Arm==sum:
    print(num,"it is a Armstrong number")    
else:
    print(num,"it is a not Armstrong number")    
    