from collections import Counter
s=input()
d=Counter()
for i in s:
    d[i]+=1
flag=False
vari=""
for i in d:
    if(d[i]%2==1):
        if(flag==False):
            flag=True
            vari=i
        else:
            print("NO SOLUTION")
            exit()
s=""
for i in d:
    s+=i*(d[i]//2)
s=s+vari+s[::-1]
print(s)
    
