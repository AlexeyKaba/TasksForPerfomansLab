import math
import sys
import re

with open ('{}'.format(sys.argv[1]),'r') as f1:
    file1=f1.read()

num_cor=re.findall(r'\d+',file1)
a=float(num_cor[0])
b=float(num_cor[1])
r=float(num_cor[2])

xy=[]
with open('{}'.format(sys.argv[2]),'r') as f2:
    file2=f2.read()

xy=re.findall(r'\d+',file2)
answer=[]
for i in range(1,len(xy),2):
    x=float(xy[i-1])
    y=float(xy[i])
    if (math.sqrt((x-a)**2)+math.sqrt((y-b)**2)<math.sqrt(r**2)):
        answer.append(1)
    elif (math.sqrt((x-a)**2)+math.sqrt((y-b)**2)==math.sqrt(r**2)):
        answer.append(0)
    else:
        answer.append(2)

for i in range(len(answer)):
    print(answer[i],'\n')
