class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(nlogk), O(n)
        heap = []
        hashmp = {}
        for n in nums:
            hashmp[n] = hashmp.get(n, 0) + 1

        for key, val in hashmp.items():
            heapq.heappush(heap, (-val, key))

        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])

        return res 
        