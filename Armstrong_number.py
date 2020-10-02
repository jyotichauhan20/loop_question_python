num=int(input("enter the number"))
sum=0
Arm=num
while Arm>0:
    digit=Arm%10
    sum=sum+digit**3
    Arm=Arm//10
if num==sum:
    print(num,"it is a Armstrong number")
else:
    print(num,"it is not Armstrong number")
            
