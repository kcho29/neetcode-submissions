import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            res = -heapq.heappop(stones) + heapq.heappop(stones)
            if res != 0:
                heapq.heappush(stones, -res)
        return -stones[0]