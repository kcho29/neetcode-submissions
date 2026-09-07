class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        if (len(nums) == 0 ):
            return 0 
        maxlen = 1
        for n in nums:
            if n-1 not in nset:
                cur = 1
                j = n+1
                while j in nset:
                    j += 1
                    cur += 1
                    maxlen = max(maxlen, cur)
        return maxlen
