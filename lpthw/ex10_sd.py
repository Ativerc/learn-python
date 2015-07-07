tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
#Using a single \ for backslash still works for this
#Dunno why Zed used ""I'm \\ a \\ cat.""
backslash_cat = "I'm \ a \ cat."

#Using \t for Lists....Hmmm
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#How do I make print "printer is down?! %s %r" work? 
#Say I wanna debug the program and I want to insert %r in some print statements. Can I do that where there's already a %s there?


#%r is for debugging. It will make everything print "as shown"


#\\     Backslash
#\'     Single quote
#\"     Double doute
#\a     ASCII bell (BEL)
#\b 	ASCII backspace (BS)
#\f 	ASCII formfeed (FF)
#\n 	ASCII linefeed (LF)
#\N{name} 	Character named name in the Unicode database (Unicode only)
#\r ASCII 	Carriage Return (CR)
#\t ASCII 	Horizontal Tab (TAB)
#\uxxxx 	Character with 16-bit hex value xxxx (Unicode only)
#\Uxxxxxxxx 	Character with 32-bit hex value xxxxxxxx (Unicode only)
#\v 	ASCII vertical tab (VT)
#\ooo 	Character with octal value ooo
#\xhh 	Character with hex value hh 

