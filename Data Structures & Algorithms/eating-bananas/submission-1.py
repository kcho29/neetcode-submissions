class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAllBananas(bans, rate, h):
            return sum(-(-b//rate) for b in bans) <= h
        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2
            if canEatAllBananas(piles, mid, h):
                high = mid
            else:
                low = mid + 1
        return low