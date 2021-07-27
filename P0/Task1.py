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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

numbers1 = [record[0] for record in texts]
numbers2 = [record[1] for record in texts]
numbers3 = [record[0] for record in calls]
numbers4 = [record[1] for record in calls]
numbers = numbers1 + numbers2 + numbers3 + numbers4
num_counts = list(set(numbers))
print(f"There are {len(num_counts)} different telephone numbers in the records.")