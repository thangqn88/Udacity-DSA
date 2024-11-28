<!--
Problem 1: Square Root of an Integer

Provide an explanation for your answer, clearly organizing your thoughts into 
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->

### Reasoning behind of decisions.
Apply the idea of Binary Search to finding the closest number n that n*n <= x (x is the input value)

### Time complexity
O(logn): As the general binary search, the BigO will be O(logn)

### Space complexity
O(1): The source code only use the fix amount of space for variables: low, high, mid