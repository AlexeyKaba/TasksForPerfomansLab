import argparse
import sys
import re

parser=argparse.ArgumentParser(description="The fourth task")
parser.add_argument('-f','--file',required=True,type=argparse.FileType(),help='File with numbers for our array')
args=parser.parse_args(sys.argv[1:])

f=args.file.read()
def number(c):
    try:
        float(c)
        return True
    except ValueError:
        return False
nums=[]
answer=[]
nums = re.findall(r'\d+',f)
print(nums)
for i in nums:
    n=int(i)
    c=0
    for j in range(len(nums)):
        if nums[j]!=n:
            c=c+abs(int(nums[j])-n)
        else:
            continue
    answer.append(c)

print(min(answer))