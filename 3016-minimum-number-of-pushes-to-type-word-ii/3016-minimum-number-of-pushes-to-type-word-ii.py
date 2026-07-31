import heapq as h
from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        count, q = Counter(word), []
        for i in count.values():
            q.append(-i)
        h.heapify(q)
        ret,i = 0,0
        while len(q)>0:
            ret += (-h.heappop(q))*(1+(i//8))
            i += 1
        return ret





        