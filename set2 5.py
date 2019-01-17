g=raw_input()
k=g.split()
a=int(k[0])
b=int(k[1])
k=a+1
str=""
while k<b:
    if k%2==0:
        print k," ",
    k=k+1
print str
