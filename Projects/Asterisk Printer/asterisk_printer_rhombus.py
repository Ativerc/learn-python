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
