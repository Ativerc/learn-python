x= int(raw_input('Enter a number:')) #not converting to int throws an error because
#range expects range(int, int)


for j in range(x,0,-1):
        print " "*j,
for k in range(1,x+1):
        print "*"*k
