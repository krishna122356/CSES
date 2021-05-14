n=int(input())
if(n%4==1)or(n%4==2):
    print("NO")
else:
    c=[]
    d=[]
    m=0
    if(n%4==3):
        c=[1,2]
        d=[3]
        m=3
    for i in range(n//4):
        d.append(m+1)
        d.append(m+4)
        c.append(m+2)
        c.append(m+3)
        m+=4
    print("YES")
    print(len(d))
    print(*d)
    print(len(c))
    print(*c)
    