class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1]

        for i in nums:
            forward.append(forward[-1]*i)
        
        backward = [1]
        for j in nums[-1::-1]:
            backward.insert(0, backward[0] * j)
        
        # [1, 1, 2, 8, 48]
        # [48, 48, 24, 6, 1]

        out = []
        for i in range(len(nums)):
            out.append(forward[i] * backward[i+1])
        return out