from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsCount = Counter(nums)

        for key, val in numsCount.items():
            if val >= len(nums)/2:
                return key
        