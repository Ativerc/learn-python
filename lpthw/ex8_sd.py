#No arguments given for the 4 format specifiers
formatter = "%r %r %r %r"

#This is cool. I am printing the value of variable formatter but
#I am putting in arguments for the format specifiers.
print formatter % (1, 2, 3, 4)# got it!
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
#This one^ looks cool. I am passing the "%r %r %r %r", i.e.
#the value of 'formatter', each time for the 4 fspecifiers.


#Zed Shaw doesn't break the 80 character per line for this...
#I will start doing that. Wait I have been doing that.
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

#Comma works, but where does it come from? Like where did I miss reading 
#about it?
#Did I miss something else?
