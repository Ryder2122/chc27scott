#functions.py 



def foo ():
    
    #1 def keyword. this tells the python code interperter that you are about to specify a funtion 
    #2 function name. this is the name of the routine that you to use. Example foo is the name \
    #3 paramenter list. are you inrputs of your function, and do they go inside the () 
    
    
    print ("bar")

foo()  # remember when you are usin g this functoin you must end trhat funtion name with the parathensis 

def add(x,y):
    #1 def keyword. functionn name: add 3. paramenter x,y 
    #how paramneters behave: they are just placeholders for values that we  can plug in later
    print(x + y) 

add(6,7) #now i want to use this funtion 
add("foo", "bar")      # we can add two stings togtehr as well 
#add ("hello",5) this is goin to be a type error 


# 6 and 7 get plugged in for x and y and adsd them togteher to make 13 add and print x + y 
# 6 and 7 arent paramneters and instead called arguments 

# what isi a fuhntoin call?    when you are running a program, the program has a concept called "ownership" 

