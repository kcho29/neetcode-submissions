class Solution:
    def compress(self, chars: List[str]) -> int:
        out = ''
        curChar = ''
        curLen = 0
        for ch in chars:
            if ch == curChar:
                curLen += 1
            else:

                if curLen == 1:
                    out += curChar
                elif curChar != "":
                    out += curChar + str(curLen)
                curChar = ch
                curLen = 1
        if curLen != 1:

            out += curChar + str(curLen)
        else:
            out += curChar
    
        chars[:] = list(out)
        return len(chars)