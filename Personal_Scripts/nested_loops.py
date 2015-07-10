#This shows how nested loops work
#This shows how print statement can be used for debugging

for i in range (7,1,-1):
    print 'i=',i
    for j in range(1,i):
        print '*' #this is a bit unnecessary
        print '\t j=',j
        for k in range(i,j,-1):
            print '*' #this too is unnecessary
            print '\t \t k=',k

    print '*'*21 #marks when i loop ends
