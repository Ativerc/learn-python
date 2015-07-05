#Above each line, use the # to write a comment to yourself explaining what the line does.


#printing "I will now count mu chickens:"
print "I will now count my chickens:"

#No newline character needed? That's odd!!
#printing "Hens", and the expression is computed. The lack of brackets makes the interpreter compute 30/6 first.
#No spaces but still space gets printed between Hens and 25 + 30/6
print "Hens",25 + 30 / 6
#Adding line 
print 75 % 4

# Precedence of operators - PEMDAS && Left to Right 
#Scanning the expressionfrom left to right, using PEMDAS, * hits first, so 25 * 3 is computed = 75
# Now assuming % having the same position in PEMDAS as / , so, 75 %4 is computed next. Which equals 3
#Next is the subtraction, so 100-3 = 97.
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

#??

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
