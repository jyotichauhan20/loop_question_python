
i=0
while i<=1000:
    j=1
    sum=0
    while j<i:
        if i%j==0:
           sum=sum+j
        j=j+1
    if sum==i:
        print(i)
    i=i+1

