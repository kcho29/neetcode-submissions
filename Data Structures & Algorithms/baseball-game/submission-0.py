class Solution:
    def calPoints(self, operations: List[str]) -> int:
        out  = []
        for op in operations:
            if op == "+":
                out.append(out[-1] + out[-2])
            elif op == "D":
                out.append(out[-1]*2)
            elif op == "C":
                out.pop(-1)
            else:
                out.append(int(op))
        return sum(out)