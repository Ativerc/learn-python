#Guess a number
#Learn how if else and elif blocks work!

print 'Guess the number!'

num = 24
uin = int(raw_input("Enter a number: ")) #could have asked for an int but
#int() converts the input to int anyway!

#Not putting a colon after the if statement gives a Syntax error
if uin == num:
    #if block starts here
    print 'You guessed it right!'
    print 'Yay!!',
    print 'you da real MVP!' 
elif uin < num:
    #elif block
    print 'Go higher....'
else:
    print "Go lower...."
