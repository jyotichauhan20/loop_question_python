num1=int(input("enter the number"))
num2=int(input("enter the numbere"))
i=1
hcf=1
while i<=num1:
    if num1%i==0 and num2%i==0:
        hcf=i
        # break
    i=i+1
print(hcf,"it is the hcf number")    
       

        
         
    
    
    