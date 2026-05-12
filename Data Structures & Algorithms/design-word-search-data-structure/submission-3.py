class TrieNode:
    def __init__(self):
        self.children = {}
        self._end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr._end = True

    def search(self, word: str) -> bool:
        def dfs(index: int, node: TrieNode) -> bool:
            if index == len(word):
                return node._end
            
            char = word[index]

            if char != '.':
                if char not in node.children:
                    return False
                return dfs(index + 1, node.children[char])
            
            for child in node.children.values():
                if dfs(index + 1, child):
                    return True
            
            return False

        return dfs(0, self.root)