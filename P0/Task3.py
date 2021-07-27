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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
#PART A
cfb = [call for call in calls if call[0][:5] == '(080)']

code1 = [call[1][call[1].find("(") + 1:call[1].find(")")] for call in cfb if '(' in call[1] and ')' in call[1]]
code2 = [call[1][:4] for call in cfb if ' ' in call[1] and call[1][0] in ['7','8','9']]
code3 = [call[1][:3] for call in cfb if call[1][:3] == '140']


codes = list(set(code1 + code2 + code3 ))
print("The numbers called by people in Bangalore have codes:")
print("\n".join(sorted(codes)))


#PART B
calls = 0
for call in cfb: 
  if call[1][:5]  == '(080)':
    calls += 1

ftf = calls / len(cfb)
print(f"{round(ftf*100,4)} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")