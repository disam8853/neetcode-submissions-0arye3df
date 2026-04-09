class Node:
    def __init__(self, key = '', val = 0):
        self.key = key
        self.val = val
        self.prev = None;
        self.next = None;

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node();
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity
        self.mp = {}        

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        node = self.mp[key]
        self.usedNode(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.mp:
            node = Node(key, value)
            nextNode = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next = nextNode
            nextNode.prev = node
            self.mp[key] = node
        else:
            node = self.mp[key]
            node.val = value
            self.usedNode(node)
        cnt = len(self.mp.values())
        if cnt > self.cap:
            lastNode = self.tail.prev
            self.tail.prev = lastNode.prev
            lastNode.prev.next = self.tail
            del self.mp[lastNode.key]
            del lastNode
        
    def usedNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

        nextNode = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nextNode
        nextNode.prev = node
