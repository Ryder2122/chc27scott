#problem 1 the hailstone problem (collatz conjucture)

x = input("enter a number: ")
x = int(x) 
while x != 1: 
    print(x) 
    if x % 2 == 0:
        x = x // 2 
    else:
        x = 3 * x + 1 
print(x)
print ("THE HAILSTONE SEQUENCE HAS ENDED")
        