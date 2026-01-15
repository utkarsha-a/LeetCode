'''
deque: pop and apppend take O(1), cannot use deque, as accesing randomn element will take O(n)
DLL + hashmap: correct
DLL - we can accesss element in O(n), so we use hashmap to access element in O(1)
'''
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.oldest = Node(0,0)
        self.latest = Node(0,0)
        self.oldest.next = self.latest
        self.latest.prev = self.oldest
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def remove(self, node):
        prev = node.prev
        nex = node.next
        prev.next = nex
        nex.prev = prev

    def insert(self, node):
        prev = self.latest.prev
        nex = self.latest
        prev.next = node
        nex.prev = node
        node.prev = prev
        node.next = nex        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.oldest.next
            self.remove(lru)
            del self.cache[lru.key]
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)