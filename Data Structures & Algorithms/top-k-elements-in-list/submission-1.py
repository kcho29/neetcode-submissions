from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(x[0] for x in list(sorted(Counter(nums).items(), key=lambda x: x[1]))[-k:])