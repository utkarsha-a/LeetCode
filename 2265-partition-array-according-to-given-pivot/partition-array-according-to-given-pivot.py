class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small, big, num = [], [], []

        for n in nums:
            if n<pivot:
                small.append(n)
            elif n>pivot:
                big.append(n)
            else:
                num.append(n)
        
        return small+num+big