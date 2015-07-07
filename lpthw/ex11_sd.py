#Each print statement in python ENDS with a newline.
#I may have written that it "starts" with a newline char elsewhere,
#I was wrong!
#Each print statement ends with a newline sharacter
#Putting a comma at the end of the print statement prevents newline characters
#
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
