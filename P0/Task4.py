"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import os 

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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
ts = list(set([text[0] for text in texts]))
tr = list(set([text[1] for text in texts]))
ic = list(set([call[1] for call in calls]))
oc = list(set([call[0] for call in calls]))

tm = [num for num in oc if num not in ts and num not in tr and num not in ic]
print("These numbers could be telemarketers: ")
print("\n".join(sorted(list(set(tm)))))

