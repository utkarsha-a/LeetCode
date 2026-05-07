class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        minHeap = []
        n = len(nums)
        for i in range(n):
            heapq.heappush(minHeap, nums[i])

            if len(minHeap)>k:
                heapq.heappop(minHeap)
        return minHeap[0]
        '''

        heapq.heapify(nums)
        while len(nums)>k:
            heapq.heappop(nums)

        return nums[0]
        