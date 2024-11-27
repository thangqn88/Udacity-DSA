
## Reasoning Behind Decisions:
This is the recursion process, the source will scan each item, if the item is file, we append value to list, if the item is directory, we need to go deeper by continue calling the current function.

## Time Efficiency:
The Time complexity is depends on width(w) and depth(d) of the directory.
Result of BigO will be O(w*d)


## Space Efficiency:
The Space complexity is depends on the number of items return (folders and files can be found) => O(w+d)