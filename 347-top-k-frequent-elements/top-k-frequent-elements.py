import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        heap=[]
        num=sorted(nums)

        ns=Counter(num)
        for key, val in ns.items():
            if len(heap)<k:
                heapq.heappush(heap,(val,key))
            else:
                heapq.heappushpop(heap,(val,key))
        return[h[1] for h in heap]



        