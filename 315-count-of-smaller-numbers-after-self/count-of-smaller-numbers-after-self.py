class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(set(nums))
        rank = {num: i + 1 for i, num in enumerate(sorted_nums)}
        BIT = [0] * (len(sorted_nums) + 1)
         
        def update(index, value):
            while index < len(BIT):
                BIT[index] += value
                index += index & -index

        def query(index):
            sum = 0
            while index > 0:
                sum += BIT[index]
                index -= index & -index
            return sum

        counts = []
        for num in reversed(nums):
            counts.append(query(rank[num] - 1))
            update(rank[num], 1)

        return counts[::-1]  






        