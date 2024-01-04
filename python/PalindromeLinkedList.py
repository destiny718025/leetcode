# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        cur = None
        while slow:
            next, slow.next = slow.next, cur
            slow, cur = next, slow

        while cur:
            if cur.val != head.val:
                return False
            cur = cur.next
            head = head.next

        return True