# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return 
        
        p1 = head
        p2 = head
        while p2.next is not None and p2.next.next is not None:
            p1 = p1.next
            p2 = p2.next.next
        
        second = p1.next
        p1.next = None
        temp = None

        while second is not None:
            next_node = second.next
            second.next = temp
            temp = second
            second = next_node

        
        first = head
        second = temp

        while second is not None:
            next_first = first.next
            next_second = second.next

            first.next = second
            second.next = next_first

            first = next_first
            second = next_second

