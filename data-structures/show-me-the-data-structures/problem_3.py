import heapq
from collections import  Counter

# Huffman Tree Node
class HuffmanNode:

    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other: 'HuffmanNode') -> bool:
        return self.freq < other.freq

def build_huffman_tree(data):
    # Calculate frequencies by using Counter
    freq = Counter(data)

    # Create a priority queue (min-heap)
    heap = [HuffmanNode(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)

    # Build the Huffman Tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Merge two nodes
        merged = HuffmanNode(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)
    return heap[0]

def generate_huffman_codes(node, code="", huffman_codes={}):
    # Base case: leaf node
    if node.char is not None:
        huffman_codes[node.char] = code or "0"
        return

    if node.left:
        generate_huffman_codes(node.left, code + "0", huffman_codes)
    if node.right:
        generate_huffman_codes(node.right, code + "1", huffman_codes)

    return huffman_codes

def huffman_encoding(data):
    if data == "":
        print("Empty string")
        return "", None
    
    if len(set(data)) == 1:
        encoded_data = "0" * len(data)
        root = HuffmanNode(data[0], len(data))
        return encoded_data, root
    
    # Build Huffman Tree
    tree_root = build_huffman_tree(data)
    # Generate codes
    huffman_codes = generate_huffman_codes(tree_root)

    # Encode the data
    encoded_data = "".join(huffman_codes[char] for char in data)
    return encoded_data, tree_root

def huffman_decoding(encoded_data, tree_root):
    # If the encoded data is empty or the tree is empty
    if not encoded_data or not tree_root:
        return ""
    
    # If the tree has only one node
    if tree_root.left is None and tree_root.right is None:
        return tree_root.char * len(encoded_data)
    
    decoded = []
    node = tree_root
    for bit in encoded_data:
        node = node.left if bit == "0" else node.right
        # If leaf node is reached
        if node.char is not None:
            decoded.append(node.char)
            node = tree_root  # Restart at the root

    return "".join(decoded)


# Main Function
if __name__ == "__main__":
    # Test Case 1: Standard test case
    print("\nTest Case 1: Standard sentence")
    sentence = "Huffman coding is fun!"
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    # Test Case 2: Edge case with empty string
    print("\nTest Case 2: Empty string")
    sentence = ""
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    # Test Case 3: Edge case with single character
    print("\nTest Case 3: Single character")
    sentence = "aaaaa"
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data