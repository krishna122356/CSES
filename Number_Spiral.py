t=int(input())
for __ in range(t):
    y,x=map(int,input().split())
    if(x>=y):
        if(x%2==1):
            x=x*x
            print(x-y+1)
        else:
            x=(x-1)*(x-1)+1
            print(x+y-1)
    else:
        if(y%2==0):
            y=y*y
            print(y-x+1)
        else:
            y=(y-1)*(y-1)+1
            print(y+x-1)

