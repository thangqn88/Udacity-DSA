<!--
Problem 7: Request Routing in a Web Server with a Trie

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
The basic idea is to implement a HTTP Router with response handlers in the form of strings. 
The key data structure is a Trie, whose nodes store a part of the url (i.e http path) and a string to ensure we got the right handler for the http request.

The program uses three classes: Router, RouteTrie and RouteTrieNode. The Router class wraps the RouteTrie and provides the public methods of the HTTP Router interface.

### Time complexity
O(n) where n is the number of parts in the url path.

### Space complexcity
O(n)