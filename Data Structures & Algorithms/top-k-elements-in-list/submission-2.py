from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return list(x[0] for x in list(sorted(Counter(nums).items(), key=lambda x: x[1]))[-k:])

        # bucket sort

        buckets = [[] for i in range(len(nums)+1)]

        for key, v in Counter(nums).items():
            buckets[v].append(key)
        
        out = []
        i = len(nums)-1
        while len(out) < k:
            out += buckets[i]
            i -= 1
            
        return out
