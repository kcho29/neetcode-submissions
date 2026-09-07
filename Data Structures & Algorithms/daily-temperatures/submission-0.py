class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stack = []

        for i,k in enumerate(temperatures):
            while stack and stack[-1][1] < k:
                res = stack.pop()
                out[res[0]] = i-res[0]
            stack.append((i,k))

        return out
                