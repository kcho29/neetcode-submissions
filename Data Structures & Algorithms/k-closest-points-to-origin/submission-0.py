import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Idea: max heap of length k. as we build, if len == k check each insert 
        # and only push if length < top

        heap = []
        heapq.heapify(heap)

        for point in points:
            x1, y1= point[0], point[0]
            if len(heap) == k:
                if math.sqrt((x1)**2 + (y1)**2) < heap[0][0]:
                    heapq.heappop()
                    heapq.heappush(heap,(math.sqrt((x1)**2 + (y1)**2), point))
            else:
                heapq.heappush(heap,(math.sqrt((x1)**2 + (y1)**2), point))
        return [x[1] for x in heap]