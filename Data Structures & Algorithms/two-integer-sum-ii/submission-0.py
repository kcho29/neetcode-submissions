class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        cursum = numbers[left] + numbers[right]
        while cursum != target:
            if cursum < target:
                left += 1
            elif cursum > target:
                right -= 1
            cursum = numbers[left] + numbers[right]
        return [left+1, right+1]
            