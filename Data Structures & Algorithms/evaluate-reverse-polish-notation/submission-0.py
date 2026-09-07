class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def helper(tokens):
            first, second, third = tokens.pop(-1), int(tokens.pop(-1)), tokens[-1]
            if third.isnumeric():
                third = int(third)
                if first == "-":
                    return second - third
                if first == "+":
                    return second + third
                if first == "*":
                    return second * third
                if first == "/":
                    return second // third
            if first == "-":
                return -second + helper(tokens)
            if first == "/":
                return helper(tokens) / second
            if first == "+":
                return helper(tokens) + second
            if first == "*":
                return helper(tokens) * second
        
        return helper(tokens)
