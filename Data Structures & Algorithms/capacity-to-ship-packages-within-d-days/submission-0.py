class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        def check(limit):
            curweight = 0
            out = 1
            for i in weights:
                if curweight + i <= limit:
                    curweight += i
                else:
                    curweight = i
                    out += 1
            return out


        while low < high:
            mid = (low + high) // 2
            if check(mid) <= days:
                high = mid
            else:
                low = mid + 1

        return low

