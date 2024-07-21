class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char):

        self.char = char

        self.is_end = False

        self.children = {}


class Trie(object):

    def __init__(self):

        self.root = TrieNode("")

    def insert(self, word):
        """Insert a word into the trie"""
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:

                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_end = True

    def dfs(self, node, prefix):

        if node.is_end:
            self.output.append((prefix + node.char))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, x):

        self.output = []
        node = self.root

        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        self.dfs(node, x[:-1])
        return sorted(self.output, key=lambda x: x[1])

    def delete(self, x):

        node = self.root
        counter = 0
        for char in x:
            if char in node.children:
                if len(node.children) > 1:
                    node = node.children[char]
                    if len(node.children) == 1:
                        node.children = {}
                        break
                    if node.children == {}:
                        node = self.root
                        counter = 0
                        for char2 in x[:-1]:
                            counter += 1
                            node = node.children[char2]
                        node.children.pop(x[counter])
                else:
                    node = node.children[char]

