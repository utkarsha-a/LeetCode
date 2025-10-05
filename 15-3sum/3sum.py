class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            lo = i+1
            hi = n-1

            while lo<hi:
                summ = nums[i] + nums[lo] + nums[hi]
                if summ == 0:
                    res.append((nums[i], nums[lo], nums[hi]))
                    lo += 1
                    hi -= 1
                    while lo<hi and nums[lo]==nums[lo-1]:
                        lo+= 1
                    while lo<hi and nums[hi]==nums[hi+1]:
                        hi-=1
                elif summ>0:
                    hi -= 1
                else:
                    lo += 1

        return res

                

        