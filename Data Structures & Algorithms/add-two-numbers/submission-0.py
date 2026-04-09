# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        node1 = l1
        node2 = l2
        carry = False
        while node1 or node2:
            s = 1 if carry else 0
            if node1:
                s += node1.val
                node1 = node1.next
            if node2:
                s += node2.val
                node2 = node2.next
            if s > 9:
                s -= 10
                carry = True
            else:
                carry = False
            newNode = ListNode(s)
            prev.next = newNode
            prev = newNode
            
        if carry:
            newNode = ListNode(1)
            prev.next = newNode

        return dummy.next