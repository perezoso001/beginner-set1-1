n=int(raw_input())
N=raw_input()
k=N.split()
j=int(k[0])
for i in range(0,n):
    if j>int(k[i]):
        j=int(k[i])
print j
    
    
