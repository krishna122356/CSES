k=int(input())
for i in range(1,k+1):
    if(i==1):
        print(0)
    elif(i==2):
        print(6)
    else:
        x=i*i*(i*i-1)//2
        y=4*(i-1)*(i-2)
        print(x-y)
