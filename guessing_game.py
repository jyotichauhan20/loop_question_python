
i=0
while i <=5:
    guessd_num=4
    user=int(input("enter the num=="))
    if user==guessd_num:
        print("well guess")
        break
    elif user>guessd_num:
        print("number bada hai")
    else:
        print("number chota h")
    # print("guess again")
    i+=1