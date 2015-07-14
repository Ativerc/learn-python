x= int(raw_input('Enter a number:')) #not converting to int throws an error because
#range expects range(int, int)

for i in range(0,x+1):
    print i
    for j in range(0,i):
        print i
        print " "*(i-1)
        for k in range(0,i):
            print "*"*(i)
