#asterisk printer 1/4 functions

def patt(x):
    for i in range(1,x+1):
        print ' '*((x+1)-i) + '*'*i

x = int(raw_input("Enter the no. of rows: \n"))

patt (x)
