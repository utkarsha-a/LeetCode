class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #O(n), O(n)
        hashmp = {}
        for n in nums:
            hashmp[n] = hashmp.get(n, 0) + 1
        freq = [[] for _ in range(len(nums)+1)]
        for n, f in hashmp.items():
            freq[f].append(n)
        res = []
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
        '''
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
        '''