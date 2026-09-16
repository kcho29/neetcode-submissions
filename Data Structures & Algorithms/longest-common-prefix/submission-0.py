class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = ""

        for i in range(len(strs[0])):
            out += strs[0][i]
            for st in strs[1:]:
                if i == len(st) or st[i] != out[i]:
                    return out[:-1]
        return out