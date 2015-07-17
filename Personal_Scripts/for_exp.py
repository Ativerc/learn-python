print "for i in range(0,4)"
for i in range(0,4):
    print i

print "for i in range(0,5)"
for i in range(0,5):
    print i

print "for i in range (1,4)"
for i in range (1,4):
    print i

print "for i in range (1,5)"
for i in range (1,5):
    print i

x = int(raw_input("Enter int: "))

print "for i in range(0,x+1)"
for i in range(0,x+1):
    print i

print "for i in range(x+1,0,-1), Reverse Counter"
for i in range(x,0,-1):
    print i

print "for j in range(x-1,0,-1):"
for j in range(x-1,0,-1):
    print j

print "for i in range(1,x+1):"
for i in range(1,x+1):
    print i


print "Nested Loop"
print
for i in range(0,x+1):
    print "i=",i
    for j in range(x,0,-1):
        print "  j=",j

print "Nested Loop 2 x=",x
for i in range(1,x+1):
    print "i=",i
    for j in range(x,0,-1):
        print "  j=",j,
        for k in range(1,i+1):
            print "    k=", k
