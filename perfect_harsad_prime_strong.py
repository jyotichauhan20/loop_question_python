num=int(input("enter a number"))
i=0
empty=[ ]
while i<num:
    num2=int(input("enter a number"))
    empty.append(num2)
    i=i+1
print(empty)
prime=["prime"]
harshad=["harsad" ]
perfect=[ "perfect"]
strong=["strong"]
i=0
while i<len(empty):
    k=1
    j=0
    while k<empty[i]:
        if empty[i]%k==0:
            j=j+1
        k=k+1
    if j==1:
        prime.append(empty[i])
    
    rem=empty[i]
    sum=0
    while rem>0:
        n=rem%10
        sum=sum+n
        rem=rem//10
    if empty[i]%sum==0:
        harshad.append(empty[i])
    m=1
    sum=0
    while m < empty[i]:
        if empty[i]%m==0:
            sum=sum+m
        m=m+1
    if sum==empty[i]:
        perfect.append(empty[i])
    
    d=empty[i]
    sum3=0
    while d>0:
        x=1
        fact=0
        rem=empty[i]%10
        while x<=rem:
            fact=fact*x
            x=x+1
        sum3=sum3+fact
        d=d//10
    if d==sum3:
        strong.append(empty[i])
    i=i+1
print(strong)
print(perfect)
print(prime)
print(harshad)