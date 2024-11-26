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

# Part A
def get_area_code(phoneNumber):
    if phoneNumber.startswith('('):
        return phoneNumber.split(')')[0] + ')'
    elif phoneNumber.startswith('140'):
        return '140'
    elif phoneNumber.startswith('7') or phoneNumber.startswith('8') or phoneNumber.startswith('9'):
        return phoneNumber[:4]
    
def get_distinct_codes_called_by_bangalore(calls):
    codes = set()
    for c in calls:
        if c[0].startswith('(080)'):
            areaCode = get_area_code(c[1])
            codes.add(areaCode)
    return sorted(codes)

list_of_codes = get_distinct_codes_called_by_bangalore(calls)
print('The numbers called by people in Bangalore have codes:')
for called_code in list_of_codes:
    print(called_code)

# Part B
def is_bangalore_number(phoneNumber):
    return phoneNumber.startswith('(080)')

def is_fixed_line_number(phoneNumber):
    return phoneNumber.startswith('(')

def get_percentage_calls_between_bangalore(calls):
    count_within_bangalore = 0
    count_from_bangalore = 0  
    for c in calls:
        if is_bangalore_number(c[0]):
            count_from_bangalore+=1
            if is_bangalore_number(c[1]):
                count_within_bangalore+=1
    return 100*count_within_bangalore/count_from_bangalore

print(f'{get_percentage_calls_between_bangalore(calls):.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')

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
