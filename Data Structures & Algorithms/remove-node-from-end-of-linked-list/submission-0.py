# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = 0
        node = head
        while node:
            node = node.next
            cnt += 1
        n = cnt - n
        cnt = 0
        node = head
        dummy = ListNode(next = head)
        prev = dummy
        while node and cnt < n:
            prev = node
            node = node.next
            cnt += 1
        prev.next = node.next
        return dummy.next