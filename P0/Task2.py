"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import os 
from collections import defaultdict

gwd = os.getcwd()
text  = os.path.join(gwd,'P0','texts.csv')
call = os.path.join(gwd,'P0','calls.csv')

with open(text, 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open(call, 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

call_len = defaultdict(int)
for caller, callee, time, duration in calls: 
    # if call[0] not in call_len.keys():
    #     call_len[call[0]] = 0
    # if call[1] not in call_len.keys():
    #     call_len[call[1]] = 0
    call_len[caller] += int(duration)
    call_len[caller] += int(duration)

lc = max(call_len,key= call_len.get)
print(f'{lc} spent the longest time, {call_len[lc]} seconds, on the phone during September 2016. ')

