class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        [1, 1, 2 , 8 , 48]
        [1, 6, 24, 48, 48]
        
        forward = [1]
        for n in nums:
            forward.append(forward[-1] * n)
        
        backward = [1]
        for n in nums[::-1]:
            backward.append(backward[-1]*n)
        
        out = []

        for i in range(len(nums)):
            out.append(forward[i] * backward[-i-2])
        return out