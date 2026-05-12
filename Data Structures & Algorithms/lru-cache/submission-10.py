class Node:
    def __init__(self, key=None, value=None, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
    
    def _remove(self, node: Node) -> None:
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def _add_to_head(self, node: Node) -> None:
        next = self.head.next
        self.head.next = node
        node.next = next
        node.prev = self.head
        next.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node_to_remove = self.cache[key]
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._remove(node_to_remove)
            self._add_to_head(new_node)

        else:
            if len(self.cache) == self.capacity:
                node_to_remove = self.tail.prev
                self._remove(node_to_remove)
                del self.cache[node_to_remove.key]
            
            # Create new node
            new = Node(key, value)
            # Add new node to head
            self._add_to_head(new)
            # Add new node to cache
            self.cache[key] = new