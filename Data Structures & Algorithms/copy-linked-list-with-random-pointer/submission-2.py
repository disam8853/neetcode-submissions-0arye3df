"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        newNode = dummy
        node = head
        mp = {}
        while node:
            newNode.next = Node(node.val)
            mp[node] = newNode.next
            newNode = newNode.next
            node = node.next
        node = head
        newNode = dummy.next
        while node:
            if node.random:
                newNode.random = mp[node.random]
            newNode = newNode.next
            node = node.next

        return dummy.next