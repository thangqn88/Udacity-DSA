<!--
Problem 2: Search in a Rotated Sorted Array

Provide an explanation for your answer, clearly organizing your thoughts into 
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->
### Reasoning behind
There are 2 sorted arrays in the input array, so we can apply binary search when we find out the pivot point.

### Time complexity
Base on the idea above and the implement of source code we can have BigO as below:
- find_pivot_index: O(logn): We use binary search algorithm to find the pivot index, n is the number items of the input list.
- rotated_array_search: use 2 function find_pivot_index O(logn), and binary_search(logk): k is the total items of the sub list
- Total: O(logn)

### Space complexity
O(1): All the functions use iteration to traverse the input array, and don't require extra storage.