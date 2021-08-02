import math
import argparse
import sys
import re

parser = argparse.ArgumentParser(description='The second task')
parser.add_argument('-f1','--file1',required=True,type=argparse.FileType(),help='File with coordinates of center and length of radius')
parser.add_argument('-f2','--file2',required=True,type=argparse.FileType(),help='File with coordinates of points')
args = parser.parse_args(sys.argv[1:])

f1=args.file1.read()
f2=args.file2.read()

num_cor=re.findall(r'\d+',f1)
a=float(num_cor[0])
b=float(num_cor[1])
r=float(num_cor[2])

xy=[]
xy=re.findall(r'\d+',f2)

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