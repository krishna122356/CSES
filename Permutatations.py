n=int(input())
if(n==1):
    print(1)
if(n==2):
    print("NO SOLUTION")
if(n==3):
    print("NO SOLUTION")
if(n>=4):
    c=[]
    for i in range(n//4):
        c.extend([4*i+2,4*i+4,4*i+1,4*i+3])
    if(n%4==1):
        c.append(c[-3]+1)
    if(n%4==2):
        c.append(c[-3]+1)
        c.insert(0,c[-1]+1)
    if(n%4==3):
        c.append(c[-3]+1)
        c.insert(0,c[-1]+1)
        c.append(c[-1]+2)
    print(*c)        
