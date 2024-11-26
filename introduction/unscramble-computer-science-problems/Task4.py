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
marketing_numbers = set()
non_marketing_numbers = set()

def get_non_marketing_numbers(texts, calls):
    for phone in texts:
        non_marketing_numbers.add(phone[0])
        non_marketing_numbers.add(phone[1])
    for call in calls:
        non_marketing_numbers.add(call[1])

    return non_marketing_numbers

def get_marketing_numbers(calls):
    for caller in calls:
        if caller[0] not in non_marketing_numbers:
            marketing_numbers.add(caller[0])
    
get_non_marketing_numbers(texts, calls)
get_marketing_numbers(calls)

print("These numbers could be telemarketers: ")
for number in sorted(marketing_numbers):
    print(number)