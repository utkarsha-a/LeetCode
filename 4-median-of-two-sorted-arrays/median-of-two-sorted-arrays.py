class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Binary Search O(log(m+n))
        A = nums1
        B = nums2
        tot = len(nums1)+len(nums2)
        half = tot//2
        
        if len(A)> len(B):
            A, B = B, A
        
        l = 0
        r = len(A)-1
        while True:
            i = (l+r)//2
            j = half-i-2

            Aleft = A[i] if i>=0 else float('-inf')
            Aright = A[i+1] if (i+1)<len(A) else float('inf')
            Bleft = B[j] if j>=0 else float('-inf')
            Bright = B[j+1] if (j+1)<len(B) else float('inf')

            if Aleft<=Bright and Bleft<=Aright:
                if tot%2==1:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright))/2
            elif Aleft>Bright:
                r = i-1
            else:
                l = i+1
        '''
        #O((m+n)log(m+n))
        i = median(sorted(nums1+nums2))
        merged = nums1+nums2
        merged.sort()
        total = len(merged)

        if total%2 == 1:
            return float(merged[total//2])
        else:
            middle1 = merged[total // 2 - 1]
            middle2 = merged[total // 2]
            return (float(middle1) + float(middle2)) / 2.0
        '''