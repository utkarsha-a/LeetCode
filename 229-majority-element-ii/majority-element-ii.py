class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        cnt1, cnt2 = 0, 0
        can1, can2 = None, None
        for n in nums:
            if n == can1:
                cnt1 += 1
            elif n == can2:
                cnt2 += 1
            elif cnt1 == 0:
                can1 = n
                cnt1 += 1
            elif cnt2 == 0:
                can2 = n
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        res = []
        for can in [can1, can2]:
            if can is not None and nums.count(can)>len(nums)//3:
                res.append(can)
        return res


        
