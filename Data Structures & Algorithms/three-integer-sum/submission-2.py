class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = set()
        for a in range(len(nums)):
            seen = set()
            for b in range(a+1, len(nums)):
                res = -nums[a]-nums[b]
                if res in seen:
                    out.add(tuple(sorted([nums[a],nums[b],res])))
                seen.add( nums[b])
        return list(out)
            