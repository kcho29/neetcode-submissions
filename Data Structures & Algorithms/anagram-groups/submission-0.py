from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        for s in strs:
            l = [0] * 26
            for ch in s:
                l[ord(ch)-ord('a')] += 1
            a[str(l)].append(s)
        return list(a.values())