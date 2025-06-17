class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        repeated = set()
        n = len(nums)
        for i in range(n):
            if nums[i] in repeated:
                repeated_ch = nums[i]
            repeated.add(nums[i])

        actual_sum = sum(nums)
        required_sum = (n*(n+1))//2
        second_ch = (required_sum-actual_sum) + repeated_ch

        return [repeated_ch, second_ch]