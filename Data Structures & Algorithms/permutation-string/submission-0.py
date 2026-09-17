from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Idea: check all sliding windows in s2 of length s1
        if len(s1) > len(s2):
            return False
        
        s1chars = [0] * 26
        for ch in s1:
            s1chars[ord(ch) - ord('a')] += 1
        left = 0
        right = len(s1) - 1
        cur = [0] * 26
        for ch in s2[:right+1]:
            cur[ord(ch)-ord('a')] += 1

        while right < len(s2):
            print(cur, '\n[]',s1chars)
            if cur == s1chars:
                return True

            cur[ord(s2[left])-ord('a')] -= 1

            left += 1
            right += 1

            if right<len(s2):
                cur[ord(s2[right])-ord('a')] += 1


        return False