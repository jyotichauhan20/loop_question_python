
Row=0
# col=0
while Row<=6:
    Col=1
    while Col<=5:        
        if ((Col == 4 and Row != 6) or (Row == 0 and Col > 2 and Col < 6) or (Row == 6 and Col == 3) or (Row == 5 and Col == 2)):  
            print("*",end="")
        else:      
            print(" ",end="") 
        Col=Col+1 
    print() 
    Row=Row+1  