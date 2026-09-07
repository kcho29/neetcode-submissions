class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = set()
        seen_a = set()
        seen_b = set()
        for a in range(len(nums)-2):
            seen = {}
            for b in range(len(nums)-1):
                res = -nums[a]-nums[b]
                if res in seen:
                    out.add(tuple(sorted([nums[a],nums[b],res])))
                seen[res] = b
        return list(out)
            