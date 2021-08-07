import sys
import re


with open('{}'.format(sys.argv[1]), 'r') as file:
    f=file.read()

def number(c):
    try:
        float(c)
        return True
    except ValueError:
        return False
nums=[]
answer=[]
nums = re.findall(r'\d+',f)
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