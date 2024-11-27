
## Union Function
The basic idea is to scan over two input linked lists and add element to the Python set.
Base on the result set, we build and return linked list.

### Reasoning Behind Decisions:
Use Python Set() to have the distinct item list and best performance than List

### Time Efficiency:
n: length of list 1
m: length of list 2
=> O(n+m): Because we iterate over two input linked lists

### Space Efficiency:
O(n+m): When all elements in both linked lists are different.

## Intersection Function
We need to convert data of input linked lists to the 2 Python set() and then compare the common items and put to the result linked list.

### Reasoning Behind Decisions:
Same as union, we use Python Set() to have better performance


### Time Efficiency:
n: length of list 1
m: length of list 2
=> O(n+m): Because we iterate over two input linked lists

### Space Efficiency:
O(n+m): When all elements in both linked lists are different.
