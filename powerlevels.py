#problem 3 powerlevels.py
num1 = input("enter number 1: ")
num1 = int(num1)
num2 = input( "enter number 2")
num2 = int(num2)
if num1 > num2: 
    print(" number 1 wins") 
elif num1 < num2:
    print("number 2 wins")
elif num1 == num2: 
    print("Its a tie")