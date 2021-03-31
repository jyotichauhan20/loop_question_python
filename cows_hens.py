def cows_hens(hens,cows):
    i=0
    while True :
        j=1
        while j<=no_of_legs:
            if i*2+j*4==no_of_legs:
                break
            j=j+1
        if i+j==no_of_heads:
            print(j,"cow",i,"hens")
            break
        i=i+1
no_of_heads=int(input("enter="))
no_of_legs=int(input("enter something="))
cows_hens(no_of_heads,no_of_legs)


