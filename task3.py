import sys
import json


with open('{}'.format(sys.argv[1]),'r') as file1:
    f1= json.loads(file1.read().replace("'",'"'))
with open('{}'.format(sys.argv[2]),'r') as file2:
    f2=json.loads(file2.read().replace("'",'"'))
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