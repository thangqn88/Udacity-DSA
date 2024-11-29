<!--
Problem 4: Dutch National Flag Problem

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
The main idea is keep the "1" at the mid of array, we only move "0" to the left and "2" to the right.
It will not require any extra space

### Time complexity
O(n): We scan all the item in array

### Space complexity
O(1) for function sort_012: Because we do not use any extra space