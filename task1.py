import sys
n=int(sys.argv[1])
m=int(sys.argv[2])
arr=[]
for i in range (1,n+1):
    arr.append(i)
arr*=int(m)
way=[]
way.append(1)
c_stop=0
c=1
step=m
while c_stop != arr[0]:
    arr+=arr
    c_stop=arr[step-c]
    way.append(c_stop)
    step+=m
    c+=1
way.pop()
print(way)