# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapq.heapify(heap)
        dummy = cur = ListNode()
        if not lists:
            return None
        for i in range(len(lists)):
            if not lists[i]:
                continue
            heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        while heap:
            val, idx, node = heapq.heappop(heap)
            cur.next = node
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
            cur = cur.next

        return dummy.next