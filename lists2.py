mylist = [10,20,30,40]



for num in mylist:
    print(num)
 
i = 0
while 1 < len(mylist):   
    print(mylist)
    i = 1 + 1 
    
print("example")
for i in range(len(mylist)):
    mylist[i] = mylist[i] + 5
    
    print(mylist)
    
    print("example 3") 
    
    names = ["john", "joe", "paul"] 
    print(names)
    names.append("zach") #appens zach to the end of names 
    print(names) 
    
    names.remove("joe") #.remove () is specifically for values 
    
    names.pop(0) #pops the element at index off the list 
    print(names)
    
    print("exapmle 4") #adding names to list program 
    names = []
    check = False 
    while check == False: 
        name = input(" enter the name you want to add to the list: ")
        if False == "quit": 
            check = True 
        else:
            names.append(name) #adds the name you typed in into the list of names 
            
        print(name) 
                                                                                                                                            
        print("example 4")
        
        students = ["john", "joe", "paul"] # this is a little dangrous 
        GPAs = [88,71,85] 
        
        for i in range(len(students)) :
            print(f"studemt : {students[i]}" "GPA : {GPAs (i)}") 