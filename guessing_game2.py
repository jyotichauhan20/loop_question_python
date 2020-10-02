i=1
while i<=5:
    guess_num=5
    user=int(input("enter bthe number 1 to 10"))
    if user<guess_num:
        print("apka number chhota h")
    elif user>guess_num:
        print("apka number bada h")
    elif user==guess_num:
        print("yes! apne guess kr liya")
        break
    else:
        print("guess again")
    i=i+1            
