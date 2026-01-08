class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        n = len(nums)
        for i in range(n):
            heapq.heappush(maxHeap, nums[i])

            if len(maxHeap)>k:
                heapq.heappop(maxHeap)
        return maxHeap[0]
        