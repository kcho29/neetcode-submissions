import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        heapq.heapify(self.left)
        heapq.heapify(self.right)
        

    def addNum(self, num: int) -> None:
        val = -heapq.heappushpop(self.left, -num)
        heapq.heappush(self.right, val)

        if len(self.left) < len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        return -self.left[0]