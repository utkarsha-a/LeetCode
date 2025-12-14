class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        '''
        self.trie = {}
        '''


    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        '''
        d = self.trie
        for c in word:
            if c not in trie:
                d[c] = {}
            d = d[c]
        d['.'] = '.'
        '''
      
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord
        '''
        d = self.trie
        for c in word:
            if c not in d:
                return False
            d = d[c]
        return '.' in d
        '''
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        '''
        d = self.trie
        for c in prefix:
            if c not in d:
                return False
            d = d[c]
        return True
        '''
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)