from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        longest = 0
        highestfreq = 0
        left = right = 0
        while right < len(s):
            freqs[s[right]] += 1
            highestfreq = max(highestfreq, freqs[s[right]])
            if right - left + 1 - highestfreq > k:
                freqs[s[left]] -= 1
                left += 1
            longest = right-left + 1
            right += 1
        return longest