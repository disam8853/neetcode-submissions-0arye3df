# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        if list1.val > list2.val:
            list1, list2 = list2, list1
        head = list1
        prev = list1
        node1 = list1.next
        node2 = list2
        while node1 and node2:
            if node1.val <= node2.val:
                prev.next = node1
                prev, node1 = node1, node1.next
            else:
                prev.next = node2
                prev, node2 = node2, node2.next
        if not node1:
            prev.next = node2
        elif not node2:
            prev.next = node1
        return head