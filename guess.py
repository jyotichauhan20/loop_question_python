i=0
guess=7
while i<=2:
    user=int(input("enter 1 to 9 "))
    if user==guess:
        print("well guess")
        break
    elif user>guess:
        print("guess numbner bada h")
    elif user<guess:
        print("guess number chhota h")
    else:
        print("try again")
    i=i+1       
