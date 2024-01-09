# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stackA = []
        stackB = []

        while headA:
            stackA.append(headA)
            headA = headA.next
        while headB:
            stackB.append(headB)
            headB = headB.next

        prev = None
        while stackA and stackB:
            nodeA = stackA.pop()
            nodeB = stackB.pop()

            if nodeA != nodeB:
                return prev
            prev = nodeA
        return prev