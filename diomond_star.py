i=1
while i<=5:
    j=5
    while j>=1:
        print(" "*j,end="")
        print(" *"*i,end="")
        print()
        j=j-1
        i=i+1
        if i==5:
            i=1
            while i<=5:
                j=5
                while j>=1:
                    print(" "*i,end="")
                    print(" *"*j,end="")
                    print()
                    j=j-1
                    i=i+1
        