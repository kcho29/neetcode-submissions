class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters = ['abc', 'def', 'ghi', 'jkl', "mno", 'pqrs', 'tuv', 'wxyz']
        out = []
        
        res = ['']

        for dig in digits:
            tmp = []
            for c in res:
                for ch in letters[int(dig)-2]:
                    tmp.append(c + ch)
            res = tmp
        return res