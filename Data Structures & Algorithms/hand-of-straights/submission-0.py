class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counts = Counter(hand)
        hand.sort()

        for num in hand:
            if counts[num]:
                for n in range(num, num + groupSize):
                    if not counts[n]:
                        return False
                    counts[n] -= 1
        return True