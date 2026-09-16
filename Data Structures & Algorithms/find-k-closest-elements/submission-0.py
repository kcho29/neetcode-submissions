class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] == x:
                left = mid
                break
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid

        right = left
        left = left - 1
        out = []
        while len(out) < k:
            if left < 0:
                out.append(arr[right])
                right += 1
                continue
            if right == len(arr):
                out.insert(0,arr[left])
                left -= 1
                continue
            if (left < 0 and right == len(arr)):
                return out
            if x - arr[left] <= arr[right] - x:
                out.insert(0, arr[left])
                left -= 1
            else:
                out.append(arr[right])
                right += 1
        return out