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

phones = []
for i in range(len(texts)):
    if texts[i][0] not in phones:
        phones.append(texts[i][0])
    if texts[i][1] not in phones:
        phones.append(texts[i][1])

for i in range(len(calls)):
    if calls[i][0] not in phones:
        phones.append(calls[i][0])
    if calls[i][1] not in phones:
        phones.append(calls[i][1])


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
print(f'There are {len(phones)} different telephone numbers in the records.')