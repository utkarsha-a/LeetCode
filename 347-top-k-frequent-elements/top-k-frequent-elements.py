class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_num = Counter(nums)
        heaps = []
        for num, freq in freq_num.items():
            heapq.heappush(heaps, (freq, num))
            if len(heaps) > k:
                heapq.heappop(heaps)
        result = [num for freq, num in heaps]
        return result
        