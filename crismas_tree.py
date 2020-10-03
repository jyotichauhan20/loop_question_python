i=1
while i<=8:
    print(" "*(8-i),end="")
    j=1
    while j<=i:
        print("* ",end="")
        j=j+1
    print()
    i=i+1
i=6
while i>=1:
        print(""*(6-i),end="   ")
        print("   *")
        i=i-1