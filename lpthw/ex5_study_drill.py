name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
#Well Hello 'Find and Replace (Ctrl + H)'....

#Multi line output using Triple quotes
print '''This is a multi-line string. This is the first line
This is the second line
This is the third!
 '''
 #%s is the format specifier for strings
print "Let's talk about %s." % name

#%d is the format specifier for strings
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."

#Multiple substitutions using format() method
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#print "There are %s and %s words here"%(teeth) This will show an error ....1
#print "There are %s words."%(teeth,teeth) This too shall show an error ....2
#The above 2 show an error because no.(format specifiers) = no.(arguments)
#In 1, no.(format specifiers) > no.(args). Error shown -> "TypeError: Not enough arguments for format string"
#in 2, no.(format specifiers) < no.(args). Error shown -> "TypeError: not all arguments converted during formatting"

print "Print color of the eyes = {} here and color of hair = {} here. .format ROCKS!!".format(eyes, hair)

#Adding line: Checking Multipleformat() methods for int and string
# Can be written as %(arg1, arg2) w/o spaces. "Mr.%s"doesn't throw an error...
print "So %d is not that heavy. Is Mr.%s sure about that?" %(weight, name)

#Testing Escape sequences
print "Testing Escape sequences"


print "Mr.\%s"
#The escape sequence is still printed. Although % sign is also printed. That is odd. I just wanted the %s to be printed.

#Printing raw strings
print r"Hi \n see the newline character does not work.."
# prefixing a string with r or R makes sure that any \n or other escape sequences are not processed

print 
# Blank print statement ^here^  is construed as a Newline character. Wait!! Every print statement in python has an invisible Newline character.

#Testing Line 43 with arguments added in format()
print "Mr.\%s" %(name)
#Substitution done successfully. But the backslash is still printed. Maybe the % doesn't need it?


#Testing it again.... with some changes
print "Mr.%"
#Prints without a problem.


#So a % sign is printed on its own, without any help of an escape sequence. If no arguments are present in format() method, the "%s" or "%d" is treated as an ordinary string.

#testing round()
nona = round(1.3332)
print nona
print "%d" %(nona)
print "%f" %(nona)
print "%3f" %(nona)
#Odd!! Shouldn't '%3f' make only 3 significant digits after decimal point?

# this line is tricky, try to get it exactly right
#Easy... format() method...just match format specifiers!!
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

