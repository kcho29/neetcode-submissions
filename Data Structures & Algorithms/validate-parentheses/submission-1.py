class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        for ch in s:
            if ch in pair:
                if len(stack) == 0 or pair[ch] != stack[-1]:
                    return False
                stack.pop(-1)
            else:
                stack.append(ch)
        return len(stack) == 0