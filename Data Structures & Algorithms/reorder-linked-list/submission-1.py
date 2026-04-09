# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        node = slow.next
        slow.next = None
        prev = None
        while node:
            tmp = node.next
            node.next = prev
            prev, node = node, tmp
        node = head
        node2 = prev
        while node2:
            tmp = node.next
            tmp2 = node2.next
            node.next = node2
            node = tmp
            node2.next = tmp
            node2 = tmp2
        return