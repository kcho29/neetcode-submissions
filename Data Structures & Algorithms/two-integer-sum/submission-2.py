class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {nums[x]:x for x in range(len(nums))}
        for i in range(len(nums)):
            if target-nums[i] in numDict and numDict[target-nums[i]] != i:
                return [i, numDict[target-nums[i]]]