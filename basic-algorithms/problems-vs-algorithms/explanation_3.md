<!--
Problem 3: Rearrange Array Digits

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
We sort the array with the descending order by using merge_sort for better performance
After sorted, we defind 2 variables num1 and num2 and pick alternating digits from the array.
num1 is filled with digits at the even indices
num2 is filled with digits at the odd indices.

### Time complexity
- Merge_sort: o(nlogn)
- Reverse list using slicing: O(n)
- TOTAL: O(nlogn + n )= O(nlogn)

### Space complexity
O(n): Because have merge_sort to return list.
