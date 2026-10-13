class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        maxheap = []

        for key, val in freq.items():
            heapq.heappush(maxheap, (-val, key))
        
        res = []
        while k:
            k -= 1
            res.append(heapq.heappop(maxheap)[1])
        
        return res