x= int(raw_input('Enter a number:')) #not converting to int throws an error because
#range expects range(int, int)

for i in range(0,x+1):
    for j in range(x,0,-1):
        print " "*j,
    for k in range(0,x+1):
        print "*"
