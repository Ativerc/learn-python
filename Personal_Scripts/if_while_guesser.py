#Guess the number but now you don't have to run the program again

num=24
val = True

while val:
    my_choiss = int(raw_input("Enter a number: "))
    #I'm just gonna copy the rest of the program from if_guesser.py
    if my_choiss == num:
    #if block starts here
        print 'You guessed it right!'
        print 'Yay!!',
        print 'you da real MVP!' 
        val = False
    elif my_choiss < num:
        #elif block
        print 'Go higher....'
    else:
        print "Go lower...."
