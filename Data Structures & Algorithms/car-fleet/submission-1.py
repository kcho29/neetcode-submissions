class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # First sort by position
        cars = sorted(zip(position, speed), reverse=True)

        # [(7,1), (4,2), (1,2), (0,1)]
        #   3       3     5      10
        stack = []
        for pos, spd in cars:
            time = (target-pos)/spd
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)