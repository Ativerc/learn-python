x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y


print "I said: %r." % x
#values of 'binary' and 'do_not' already substitued in y
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#Removing the '%r' from above gives error in line21. Hmmm... Why?
#also shows that Python has an interpreter rather than a compiler because the lines before these were executed properly.


print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#concatenation of 2 strings Got it!
print w + e
