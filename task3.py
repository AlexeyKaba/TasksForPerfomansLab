import sys
import argparse
import json

parser=argparse.ArgumentParser(description="The third task")
parser.add_argument('-t','--test', required=True, type=argparse.FileType())
parser.add_argument('-v','--values', required=True, type=argparse.FileType())

args=parser.parse_args(sys.argv[1:])
f1= json.loads(args.test.read().replace("'",'"'))

f2=json.loads(args.values.read().replace("'",'"'))
print(f1,f2)

def fn(test):
    matches = [result for result in f2['values'] if test['id']==result['id']]
    if len(matches)>0:
        test['value'] = matches[0]['value']
    if 'values' in test.keys():
        for innerTest in test['values']:
            fn(innerTest)

for test in f1['tests']:
    fn(test)

report=f1['tests']
jsonReport=json.dumps(report)
with open("report.json","w") as f3:
    f3.write(jsonReport)