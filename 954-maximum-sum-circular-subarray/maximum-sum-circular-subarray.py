class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0

        maxSum = curMax = nums[0]
        minSum = curMin = nums[0]

        for num in nums[1:]:
            curMax = max(num, curMax+num)
            maxSum = max(maxSum, curMax)

            curMin = min(num, curMin+num)
            minSum = min(minSum, curMin)

            total += num
        total += nums[0]

        if maxSum<0:
            return maxSum
        else:
            return max(maxSum, total-minSum)

        