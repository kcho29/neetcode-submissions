class Solution:
    def countSeniors(self, details: List[str]) -> int:
        out = 0
        for person in details:
            if int(person[-4:-2]) > 60:
                out += 1
        return out