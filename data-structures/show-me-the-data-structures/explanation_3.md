
## Reasoning Behind Decisions:
Min-Heap ensures quick access to the smallest frequencies during tree construction, with operations in O(logn)
Binary Tree represents the Huffman tree, enabling prefix-based encoding for each character.
Dictionary stores character-to-binary mappings, allowing fast O(1) lookup during encoding.
Strings/Lists manage encoded binary data compactly for easy manipulation.

## Time Efficiency:
Node - class with only one __init__ function, O(1)
build_huffman_tree -> O(clogc) - Trging nodes in the heap and invoke heap methods.
generate_huffman_codes => O(c) - Tree traversal to assign binary codes to c characters.
huffman_encoding => O(n) This method has one independent on input data.
huffman_decoding => O(c) This function also has a complexity of O(c)
Total => O(n + clogc) n: input size, c:number of unique characters

## Space Efficiency:
build_huffman_tree -> O(c)
generate_huffman_codes => O(c).
huffman_encoding => O(n) n: input size
huffman_decoding => O(c)
Total => O(n + c) n: input size, c:number of unique characters