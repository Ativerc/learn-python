#Each print statement in python ENDS with a newline.
#I may have written that it "starts" with a newline char elsewhere,
#I was wrong!
#Each print statement ends with a newline sharacter
#Putting a comma at the end of the print statement prevents newline characters

#How raw_input() works? raw_input takes in input as strings.
#You can convert it to int with int(raw_input())
#Further you can give the value to a variable using 
# for e.g. x = int(raw_input())
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
