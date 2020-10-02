num=int(input("enter the number"))
s=0
i=0
Arm=num
while i<num:
    digit=num%10
    s=s+digit**3
    num=num//10
if s==Arm:
    print(s,"it is Armstrong number")
else:
    print(num,"it is not Armstrong number")        

    
