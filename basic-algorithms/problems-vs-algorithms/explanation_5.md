<!--
Problem 5: Autocomplete with Tries

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
As requirement from problem, the Trie is the linked set of nodes, each node (the TrieNode) contains
- is_word (boolean)
- children (dictionary) to store childrn of a node. We use dictionary to have dynamic memory allocate base on input word list.

For the suffixes(suffix) function, it calls a recursive function and will return a list of all complete words with a input prefix.


### Time complexity
Insert: O(n), n is length of the word in word list
Find: O(s), s is length of search string
Total: O(n*s) 

### Space complexicy
Total: O(n)