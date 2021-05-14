s=input()
count=0
maxi=0
curr=""
for i in s:
    if(i==s):
        count+=1
    else:
        s=i
        maxi=max(maxi,count)
        count=1
maxi=max(maxi,count)
print(maxi)
