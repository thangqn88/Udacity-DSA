
## Reasoning Behind Decisions:
As the requirements from the LRU cache, my solution will use the OrderedDict(), it's the Dict but we can keep the ordered to track the history. All the operations in OrderedDict have O(1) time.



## Time Efficiency:
Performance is O(1) for get() and set() base on performance of Dict method.

## Space Efficiency:
The space depends on the size of Cache, it will be O(n)