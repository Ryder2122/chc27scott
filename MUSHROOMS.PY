# PROBLEM 2 (mushrooms.py) 

small = []
medium = []
Massive = [] 

print(" print you mushrooms size on at a time") 
print("type 'stop' when you are finished \n") 

check = False 
while check == False: 
    user_input = input(" enter mushrrom size ").strip().lower() 
    if user_input == "stop": 
        check = True 
    if user_input.isnumeric():  
        size = int(user_input) 
        if size < 100:
            small.append(size) 
        elif size < 200: 
            medium.append(size) 
        else: 
            Massive.append(size) 
    else: 
        print(f"'{user_input} is not a valid number. please enter a number or type 'stop' ")  

print("\n. small mushrooms", small ) 
print("medium mushrooms", medium) 
print(" Massive mushrooms" , Massive)