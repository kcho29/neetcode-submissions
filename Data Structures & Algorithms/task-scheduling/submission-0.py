from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks).values()
        biggest= max(counts)
        freq = sum(1 for i in counts if i == biggest)

        min_time = (biggest - 1) * (n+1) + freq
        return max(len(tasks), min_time)

                