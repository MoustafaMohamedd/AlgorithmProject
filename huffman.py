# Importing defaultdict from collections module
from collections import defaultdict

# Function to generate Huffman codes for characters
def huffman_code_tree(node, left=True, binString=''):
    """
    Generate Huffman codes recursively for characters in the Huffman tree.

    Args:
    - node: Node representing a character or an internal node in the Huffman tree
    - left: Boolean indicating if the current node is a left child (default is True)
    - binString: String representing the Huffman code for the character (default is an empty string)

    Returns:
    - Dictionary containing characters and their respective Huffman codes
    """
    # If the node represents a single character, return its Huffman code
    if type(node) is str:
        return {node: binString}

    # Get the left and right child nodes of the current node
    (left_child, right_child) = node.children()
    huffman_dict = {} # Initializing an empty dictionary

    # Generate Huffman codes recursively for the left and right child nodes
    # For the left child, append '0' to the current Huffman code
    huffman_dict.update(huffman_code_tree(left_child, True, binString + '0'))
    # For the right child, append '1' to the current Huffman code
    huffman_dict.update(huffman_code_tree(right_child, False, binString + '1'))
    return huffman_dict

# Calculating character frequency
string = 'BCAADDDCCACACAC'
freq = defaultdict(int)
for c in string:
    # Counting the frequency of each character in the given string
    freq[c] += 1

# Constructing the Huffman tree
nodes = sorted(freq.items(), key=lambda x: x[1], reverse=True)
# Sorting characters based on their frequencies, creating a list of tuples (character, frequency)

# Define the NodeTree class or function
class NodeTree:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def children(self):
        """
        Return the left and right child nodes of the current node.

        Returns:
        - Tuple containing the left and right child nodes.
        """
        return self.key, self.value

while len(nodes) > 1:
    # Executing this loop until there's only one node (character or combined node) left in the 'nodes' list

    # Pop the two nodes with the lowest frequencies from the sorted list 
    (key1, c1) = nodes.pop()
    (key2, c2) = nodes.pop()
    
    # Create a new node with a frequency equal to the sum of their frequencies.
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    # Sorting the nodes based on frequencies
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

# Generating Huffman codes
huffmanCode = huffman_code_tree(nodes[0][0])

# Displaying characters with their Huffman codes
print(' Char | Huffman code ')
print('----------------------')
for (char, _) in freq.items():
    # Printing each character and its corresponding Huffman code
    print(f' {char:<4} |{huffmanCode[char]:>12}')
