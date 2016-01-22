#CHANGES:
#1.From now on, I won't comment on every print statement, unless they are confusing or are a bit odd. 
#1.1But I will keep on commenting where I can break the program and the errors thrown.
#I won't upload the source code files anymore. I will upload the study drill files only.
#Will change the filename pattern from exX_study_drill.py to exX_sd.py from next commit.

print "Mary had a little lamb."
#format specifier. Removing the quotes from string, throws error "NameError: name 'snow' is not defined" 
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10  # what'd that do?
#prints the given string 10 times without \n character

print "."

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

#The output of BOTH lines 28 and 29 is "Cheese Burger" in one line
#Usually a print has a \n but the comma at the end of the first print negates the effect of the \n



