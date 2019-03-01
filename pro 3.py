a=raw_input()
b=raw_input()
a=list(a)
b=list(b)
m=len(a)
n=len(b)
if(m<n):
    l=m
    while(l<=n):
        a.append(" ")
        l=l+1
i=0
mod=0
while(i<n):
    if(a[i]==b[i]):
        i=i+1
    elif(a[i]!=b[i]):
        a[i]=str(b[i])
        mod=mod+1
        i=i+1
print mod
