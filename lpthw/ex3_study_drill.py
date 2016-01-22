#Above each line, use the # to write a comment to yourself explaining what the line does.


#printing "I will now count mu chickens:"
print "I will now count my chickens:"

#No newline character needed? That's odd!!
#printing "Hens", and the expression is computed. The lack of brackets makes the interpreter compute 30/6 first.
#No spaces but still space gets printed between Hens and 25 + 30/6
print "Hens",25 + 30 / 6
#Adding line 
print 75 % 4

# Precedence of operators - Check the bottom of this file for more details 

print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

#See Operator Precedence below....

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

# 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
# 3 + 2 + 1 - 5 + (4 % 2) - (1 / 4) + 6
# 3 + 2 + 1 - 5 + 0 - 0 + 6
# (3 + 2) + 1 - 5 + 0 + 6
# 5 + 1 - 5 + 6
# (5 + 1) - 5 + 6
# 6 - 5 + 6
# 1 + 6 
# 7

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2



#~~~~OPERATOR PRECEDENCE~~~~
#Check the Python docs - https://docs.python.org/2/reference/expressions.html#operator-precedence

#following table summarizes the operator precedences in Python, from lowest precedence (least binding) to highest precedence (most binding). Operators in the same box have the same precedence. Unless the syntax is explicitly given, operators are binary. Operators in the same box group left to right (except for comparisons, including tests, which all have the same precedence and chain from left to right — see section Comparisons — and exponentiation, which groups from right to left)

# Operator											Description
# lambda											Lambda expression
# if – else											Conditional expression
# or												Boolean OR
# and												Boolean AND
# not x												Boolean NOT
# in, not in, is, is not, <, <=, >, >=, <>, !=, ==	Comparisons, including membership tests and identity tests
# |													Bitwise OR
# ^													Bitwise XOR
# &													Bitwise AND
# <<, >>											Shifts
# +, -												Addition and subtraction
# *, /, //, %										Multiplication, division, remainder [8]
# +x, -x, ~x										Positive, negative, bitwise NOT
# **												Exponentiation [9]
# x[index], x[index:index], x(arguments...), x.attribute	Subscription, slicing, call, attribute reference
# (expressions...), [expressions...], {key: value...}, `expressions...`	Binding or tuple display, list display, dictionary display, string conversion

#Also see http://stackoverflow.com/questions/25753474/python-comparison-operators-chaining-grouping-left-to-right
#So, non-comparison operators ​*Group*​, i.e., say `w+x+y+z` => `((w+x)+y)+z`
#and ​*chaining*​ is done by comparisons only. say `w>x>y>z` => `(w>x) and (x>y) and (y>z)`

#Also in `(w>x) and (x>y) and (y>z)`, if `(w>x)` is false, then the next 2 expressions are not evaluated at all. Its because of Short-circuit evaluation.

#From ShortCircuit or McCarthy Evaluation wiki: 
#>the second argument is executed or evaluated only if the first argument does not suffice to determine the value of the expression: when the first argument of the AND function evaluates to false, the overall value must be false; and when the first argument of the OR function evaluates to true, the overall value must be true
```