# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recursively(None, head)

    def recursively(self, prev, head) -> Optional[ListNode]:
        if not head:
            return prev

        next, head.next = head.next, prev
        return self.recursively(head, next)

