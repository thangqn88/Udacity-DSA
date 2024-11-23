"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

phones = set()
for i in texts:
    phones.add(i[0])
    phones.add(i[1])
    

for i in calls:
    phones.add(i[0])
    phones.add(i[1])

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
print(f'There are {len(phones)} different telephone numbers in the records.')