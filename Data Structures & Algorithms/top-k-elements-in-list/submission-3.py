from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]

        print(Counter(nums))
        for key, val in Counter(nums).items():
            buckets[val].append(key)
        
        out = []
        
        for elmn in buckets[::-1]:
            if len(out) < k:
                out += elmn
        return out