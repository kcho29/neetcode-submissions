# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = out = ListNode()
        rem = 0
        while l1 or l2:
            lval = 0
            l2val = 0
            if l1:
                lval = l1.val
            if l2:
                l2val = l2.val
            cur = lval + l2val + rem
            if cur >= 10:
                rem = 1
                cur -= 10
            else:
                rem = 0
            out.next = ListNode(val=cur)
            l1= l1.next if l1 else None
            l2 = l2.next if l2 else None
            out = out.next
        if rem:
            out.next = ListNode(val=1)
        return dummy.next