from collections import Counter, namedtuple
import heapq

class Node(namedtuple("Node", ["char", "freq", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_tree(freqs):
    heap = [Node(ch, freq, None, None) for ch, freq in freqs.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        heapq.heappush(heap, Node(None, left.freq + right.freq, left, right))

    return heap[0]

def huffman_codes(tree, prefix=""):
    if tree.char is not None:
        return {tree.char: prefix}
    codes = {}
    if tree.left:
        codes.update(huffman_codes(tree.left, prefix + "0"))
    if tree.right:
        codes.update(huffman_codes(tree.right, prefix + "1"))
    return codes

def huffman_encode(data):
    freqs = Counter(data)
    tree = huffman_tree(freqs)
    codes = huffman_codes(tree)
    encoded = "".join(codes[num] for num in data)
    return codes, encoded

def huffman_decode(encoded, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    buffer = ""
    decoded = []
    for bit in encoded:
        buffer += bit
        if buffer in reverse_codes:
            decoded.append(reverse_codes[buffer])
            buffer = ""
    return decoded

# arr = [5, 7, 3, 1, 4, 1, 1]
# codes, compressed = huffman_encode(arr)

# decompressed = huffman_decode(compressed, codes)
