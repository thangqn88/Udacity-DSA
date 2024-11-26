"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

telephoneTime = {}
theChampion = ""
maxTime = 0

for i in range(len(calls)):
    if calls[i][0] in telephoneTime:
        telephoneTime[calls[i][0]] += int(calls[i][3])
    else:
        telephoneTime[calls[i][0]] = int(calls[i][3])
    if calls[i][1] in telephoneTime:
        telephoneTime[calls[i][1]] += int(calls[i][3])
    else:
        telephoneTime[calls[i][1]] = int(calls[i][3])
    if telephoneTime[calls[i][0]] > maxTime:
        maxTime = telephoneTime[calls[i][0]]
        theChampion = calls[i][0]
    if telephoneTime[calls[i][1]] > maxTime:
        maxTime = telephoneTime[calls[i][1]]
        theChampion = calls[i][1]
    

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
print(f'{theChampion} spent the longest time, {maxTime} seconds, on the phone during September 2016.')