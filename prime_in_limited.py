num=int(input("enter the number="))
i=1
count=0
while count<num:
    n=i
    c=0
    k=1
    while k<=n:
        if n%k==0:
            c=c+1
        k=k+1
    if c==2:
        print(i)
        count=count+1
    i=i+1
