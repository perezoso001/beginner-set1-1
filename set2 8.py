g=raw_input()
k=g.split()
a=int(k[0])
b=int(k[1])
k=a+1
str=""
while k<b:
    temp=k
    sum=0
    while temp>0:
        digit=temp % 10
        sum+=digit ** 3
        temp/= 10
    if k == sum:
        print k," ",
    k+=1
