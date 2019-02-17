a=int(raw_input())
ans1=""
ans=""
c=[]
i=0
k=0
while(i<a):
    b=raw_input()
    c.append(b)
    i=i+1
'''i=0
while(i<a):
    print c[i]
    i=i+1'''
i=0
while(i<a):
    for j in c:
        if k==0:
            ans=j
            k=1
        else:
            f=ans
            o=len(f)
            m=len(j)
            if(o<m):
                inc=o
            else:
                inc=m
            incre=0
            while(incre<inc):
                if f[incre]==j[incre]:
                    ans1=ans1+f[incre]
                incre=incre+1
            ans=ans1
            ans1=""
    i=i+1
print ans
