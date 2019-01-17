g=raw_input()
k=g.split()
a=int(k[0])
b=int(k[1])
for i in range(a,b):
    j=1
    flag=0
    while j<i:
        if i%j==0:
            flag=flag+1
        j=j+1
    if flag==1:
        print i," ",
