class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums)-1
        oper_count = 0
        while l<r:
            sum_pair = nums[l] + nums[r]
            if sum_pair == k:
                oper_count += 1
                l += 1
                r -= 1
            elif sum_pair > k:
                r -= 1
            else:
                l += 1

        return oper_count       