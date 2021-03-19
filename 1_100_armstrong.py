num1=int(input("enetr the number="))
num2=int(input("enter the number="))
while num1<=num2:
    s=0
    arm=num1
    count=0
    while arm>0:
        digit=arm%10
        s=s+digit**3
        arm=arm//10
    if num1==s:
        print(num1)
    num1+=1


