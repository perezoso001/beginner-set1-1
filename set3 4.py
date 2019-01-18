n=int(raw_input())
N=raw_input()
k=N.split()
l=""
for i in range(0,n):
    for j in range(0,n):
        if int(k[i])<int(k[j]):
            temp=k[i]
            k[i]=k[j]
            k[j]=temp
for i in range(0,n):
    l+=k[i]
    l+=" "
print l
    
