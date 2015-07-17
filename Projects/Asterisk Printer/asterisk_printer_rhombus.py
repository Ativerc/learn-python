def luppattern(x):
    for i in range(1,x+1):
        print ' '*((x+1)-i) + "*"*i + "*"*(i-1)
    print '*'*((x*2)+1) + ' ' + y



def ldopattern(x):
    for i in range(1, x+1):
        print ' '*i + '*'*((x+1)-i) + '*'*((x+1)-i-1)
y = raw_input("Enter Message: \n\n")
x = int(raw_input("Enter the no. of rows: \n\n") )
luppattern(x)
ldopattern(x)

#Done!!
#its nice how the pattern looks like a rhombus rather than switches on say an
#elevator call button/setup.
#Symmetry vs no symmetry huh?

#Think I will hold off from pattern builds for a couple of days..
#Read up on string manipulation, modules, and other stuff
#and get back to this next week.
#Also probably stop commenting like its my blog.
#Fun stuff planned for this weekend
