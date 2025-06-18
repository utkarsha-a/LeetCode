class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmp = {}
        sum_val = 0
        max_len = 0

        for i, num in enumerate(nums):
            if num == 1:
                sum_val += 1
            else:
                sum_val -= 1
            
            if sum_val == 0:
                max_len = i+1
            elif sum_val in hashmp:
                max_len = max(max_len, i - hashmp[sum_val])
            else:
                hashmp[sum_val] = i
            
        return max_len
        