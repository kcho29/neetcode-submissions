# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        leftseen = set()
        rightseen = set()

        while headA and headB:
            leftseen.add(headA)
            rightseen.add(headB)
            if headA in rightseen:
                return headA
            if headB in leftseen:
                return headB

            headA = headA.next
            headB = headB.next
        
        if not headA:
            while headB:
                if headB in leftseen:
                    return headB
                headB = headB.next
                
        else:
            while headA:
                if headA in rightseen:
                    return headA
                headA = headA.next
        return None