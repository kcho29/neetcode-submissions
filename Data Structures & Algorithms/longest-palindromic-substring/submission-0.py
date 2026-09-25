class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        out = ""
        for idx in range(len(s)):
            odd, even = expand(idx, idx), expand(idx, idx+1)
            if len(odd) > len(out):
                out = odd
            if len(even) > len(out):
                out = even
        return out