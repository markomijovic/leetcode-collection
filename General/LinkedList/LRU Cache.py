class DlinkedNode():
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(OrderedDict):
    
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        prev = node.prev
        nxt = node.next
        
        prev.next = nxt
        nxt.prev = prev
    
    def _move_node(self, node):
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        n = self.tail.prev
        self._remove_node(n)
        return n

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.len = 0
        self.size = 0
        self.head = DlinkedNode()
        self.tail = DlinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)
        if not node:
            return - 1
        self._move_node(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.cache.get(key, None)
        if not node:
            newNode = DlinkedNode(key, value)
            self.cache[key] = newNode
            self._add_node(newNode)
            self.size += 1
            
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        
        else:
            node.value = value
            self._move_node(node)