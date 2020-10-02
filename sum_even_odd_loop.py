num=int(input("enter the number"))
i=1
sum1=0
sum2=0
while i<=num:
    if i%2==0:
        print(i,"even")
        sum1=sum1+i
    else:
        print(i,"odd")
        sum2=sum2+i
    i=i+1
print("sum of even",sum1)
print("sum of odd",sum2)            
