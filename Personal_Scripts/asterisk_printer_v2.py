x= int(raw_input('Enter a number:')) #not converting to int throws an error because
#range expects range(int, int)
y=x
for i in range(0,x+1):
    for j in range(x-1,0,-1):
        print y
        y -=1
        print " "*j,
        print "y",
    for k in range(0,i):
        print "*"*k
