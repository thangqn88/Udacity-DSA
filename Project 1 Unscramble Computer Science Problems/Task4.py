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
marketing_numbers = []
non_marketing_numbers = []

def get_non_marketing_numbers():
    for phone in texts:
        if phone[0] not in non_marketing_numbers:
            non_marketing_numbers.append(phone[0])
        if phone[1] not in non_marketing_numbers:
            non_marketing_numbers.append(phone[1])
    for call in calls:
        if call[1] not in non_marketing_numbers:
            non_marketing_numbers.append(call[1])

    return non_marketing_numbers

def get_marketing_numbers():
    for caller in calls:
        if caller[0] not in non_marketing_numbers:
            marketing_numbers.append(caller[0])
    

print("These numbers could be telemarketers: ")
for number in marketing_numbers:
    print(number)

# Time complexity: O(n)
# Space complexity: O(n)