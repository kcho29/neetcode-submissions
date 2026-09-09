class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        out = 0
        cur = 0

        for n in nums:
            cur += n
            if cur - k in prefix:
                out += prefix[cur-k]
            if cur in prefix:
                prefix[cur] += 1
            else:
                prefix[cur] = 1
        return out