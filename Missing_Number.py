n=int(input())
c=list(map(int,input().split()))
d={}
for i in range(1,n+1):
    d[i]=1
for i in c:
    d.pop(i)
print(list(d.keys())[0])