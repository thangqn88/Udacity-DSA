<!--
Problem 6: Unsorted Integer Array

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
We only have to scan the array in a single traveral and update the min and max by comparing with previous min, max

### Time complexity
O(n) with n is the size of input array

### Space complexcity
O(1), we use two variables and no need extra memory.