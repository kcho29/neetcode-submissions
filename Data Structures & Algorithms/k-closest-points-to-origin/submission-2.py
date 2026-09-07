import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Idea: max heap of length k. as we build, if len == k check each insert 
        # and only push if length < top

        heap = []
        heapq.heapify(heap)

        for x,y in points:
            heapq.heappush(heap, (-(x**2 + y**2), x,y))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [[x,y] for d,x,y in heap]