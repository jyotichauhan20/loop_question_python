position_of_houese=int(input("enter yoyr houes position="))
position_of_appletree=int(input("enter your appletree position"))
position_of_orangetree=int(input("enter your orange tree position="))
num_of_apple=int(input("enter your nunber how many apple  felldown"))
num_of_orange=int(input("enter your number how many oranges felldown"))
i=0
count_of_apple=0
while i<num_of_apple:
    distanse=int(input("enter your apple distanse ="))
    position_of_applefelldown=position_of_appletree+distanse
    if position_of_applefelldown==position_of_houese:
        count_of_apple=count_of_apple+1
    i+=1
print(count_of_apple,"apples")

j=0
count_of_orange=0
while j<num_of_orange:
    distanse_of_orange=int(input("enter your orange distanse="))
    position_of_orangesfelldown=position_of_orangetree+distanse_of_orange
    if position_of_orangesfelldown==position_of_orangetree:
        count_of_orange=count_of_orange+1
    j+=1
print(count_of_orange,"oranges")

