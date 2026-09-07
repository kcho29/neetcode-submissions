class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        out = 0
        curletters = set()
        left = 0
        for idx, ch in enumerate(s):
            if ch in curletters:
                while s[left] != ch:
                    curletters.discard(s[left])
                    left += 1
            curletters.add(ch)
            out = max(out, len(curletters))

        return out