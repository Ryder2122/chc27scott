""" 
if i wanted a bunch of related data points, the only way way i can currently do that is by creating a bunch of individual variables 
""" 

num1 = 10
num2 = 20 

"""
what happens when our data is set tp 100 data points long? creating individual varaibles 


"""

mylist = [ 5, 10, 15, 20,] 
    #this creats our list 
print(mylist)

print(mylist[0])

print(mylist[0] * mylist[3])





for num in mylist:
    num = num + 5 
    
    print(mylist) 
    
    i = 0 
while i <= 3: 
    mylist[1] = mylist[1] + 5  
    i = i + 1 
    
    print(mylist) 
    
    