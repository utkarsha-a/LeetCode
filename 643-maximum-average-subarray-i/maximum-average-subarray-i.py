class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[:k])
        maxsum = summ

        for i in range(k,len(nums)):
            summ += nums[i]
            summ -= nums[i-k]
            maxsum = max(maxsum, summ)

        return maxsum/k

        #O(n)
        #O(1)



        