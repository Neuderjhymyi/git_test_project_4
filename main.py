import heapq
from collections import defaultdict


# Класс для создания узлов дерева Хаффмана
class HuffmanNode:
    def __init__(self, freq, char=None):
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None

    # Метод для сравнения узлов по частоте
    def __lt__(self, other):
        return self.freq < other.freq


# Функция для создания дерева Хаффмана
def build_huffman_tree(freq_dict):
    priority_queue = [HuffmanNode(freq, char) for char, freq in freq_dict.items()]
    heapq.heapify(priority_queue)
    while len(priority_queue) > 1:
        left_child = heapq.heappop(priority_queue)
        right_child = heapq.heappop(priority_queue)
        parent = HuffmanNode(left_child.freq + right_child.freq)
        parent.left = left_child
        parent.right = right_child
        heapq.heappush(priority_queue, parent)
    return priority_queue[0]


# Функция для создания словаря кодировок на основе дерева Хаффмана
def build_huffman_codes(node, prefix="", codes={}):
    if node.char is not None:
        codes[node.char] = prefix
    else:
        build_huffman_codes(node.left, prefix + "0", codes)
        build_huffman_codes(node.right, prefix + "1", codes)
    return codes


# Функция для кодирования текста с помощью словаря кодировок
def huffman_encode(text, codes):
    encoded_text = ""
    for char in text:
        encoded_text += codes[char]
    return encoded_text


# Функция для декодирования текста на основе дерева Хаффмана
def huffman_decode(encoded_text, huffman_tree):
    decoded_text = ""
    current_node = huffman_tree
    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = huffman_tree
    return decoded_text

# Пример использования
text = input("enter the text and press enter: ")

freq_dict = defaultdict(int)
for char in text:
    freq_dict[char] += 1

huffman_tree = build_huffman_tree(freq_dict)
huffman_codes = build_huffman_codes(huffman_tree)
encoded_text = huffman_encode(text, huffman_codes)
decoded_text = huffman_decode(encoded_text, huffman_tree)


print("Original text:", text)
print("#" * 60)
print("Encoded text:", encoded_text)
print("#" * 60)
print("Decoded text:", decoded_text)
