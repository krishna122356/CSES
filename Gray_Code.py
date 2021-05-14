n=int(input())
c=["0","1"]

for i in range(n-1):
    d=[]
    d.extend(c)
    c.reverse()
    d.extend(c)
    for i in range(len(d)//2):
        d[i]=d[i]+"1"
        d[len(d)-i-1]=d[len(d)-i-1]+"0"
    c=[i for i in d]
for i in c:
    print(i)
    
