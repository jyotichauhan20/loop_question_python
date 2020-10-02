num=int(input("enter the number"))
s=""
while num>0:
    rem=num%2
    s=s+str(rem)
    que=num//2
    num=que

print(s)
i= -1
revers_no=""
while i>=-(len(s)):
    revers_no =revers_no+s[i]
    i=i-1
print(revers_no)
