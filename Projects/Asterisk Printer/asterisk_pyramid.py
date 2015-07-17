def patt(x):
    for i in range(1,x+1):
       print ' '*((x+1)-i) + '*'*i + '*'*(i-1)

x= int(raw_input("Enter the no. of rows: \n"))
patt(x)

#Done!!
