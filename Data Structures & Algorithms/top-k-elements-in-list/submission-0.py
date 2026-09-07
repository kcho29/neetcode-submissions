from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return sorted(list(Counter(nums).keys()))[-k:]