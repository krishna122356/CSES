n=int(input())
c=list(map(int,input().split()))
o=0
for i in range(1,len(c)):
    if(c[i]<c[i-1]):
        o+=c[i-1]-c[i]
        c[i]=c[i-1]
print(o)