o=raw_input()
k=o.split()
N=int(k[0])
A=int(k[1])
D=int(k[2])
i=1
sum=0
while i<=N:
    j=i-1
    sum+=(A+j*D)
    i+=1
print sum
