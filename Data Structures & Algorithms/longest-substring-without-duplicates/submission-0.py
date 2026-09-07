class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 1
        left = 0
        curletters = set(s[0])
        for right in range(1,len(s)):
            while s[right] in curletters:
                curletters.remove(s[left])
                left += 1
            curletters.add(s[right])
            maxlen = max(maxlen, right-left + 1)
        return maxlen
