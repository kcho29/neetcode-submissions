class Solution:
    def isHappy(self, n: int) -> bool:
        def squareDigits(number):
            out = (number % 10)**2
            while number > 0:
                number = number // 10
                out += (number % 10)**2
            return out
        
        slow = fast = n
        while fast != 1:
            slow = squareDigits(slow)
            fast = squareDigits(squareDigits(fast))
            print(slow, fast)
            if slow == fast and fast != 1:
                return False
        return True