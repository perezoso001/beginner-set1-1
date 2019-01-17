g=int(raw_input())
i=2
flag=0
while i<g:
    if g%i==0:
        flag=flag+1
    i=i+1
if flag>=1:
    print "no"
else:
    print "yes"
