#problem 3 

print(" enter a word or phrase to see if its a palidrone or type 'see ya' to quit ")
check = False 
while check == False:
    word = input(" enter a word").strip().lower()
    if word == "see ya":  
        print("peace out lil bro") 
        check = True 

    words = word.split() 
    word_no_spaces = "".join(words)

    start = 0 
    end = len(word_no_spaces) - 1 
    anything_brainrot = True 

    while start < end: 
        if word_no_spaces[start] != word_no_spaces[end]:
            anything_brainrot = False
        start += 1
        end -= 1

    if anything_brainrot:
        print(f"'{word}' is a palindrone") 
    else: 
        print(f"'{word}is not palidrone")