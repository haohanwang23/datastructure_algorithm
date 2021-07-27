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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
ft = texts[0]
print(f'First record of texts, {ft[0]} texts {ft[1]} at time {ft[2]}')
lc = calls[-1]
print(f'Last record of calls, {lc[0]} calls {lc[1]} at time {lc[2]}, lasting {lc[3]} seconds')

