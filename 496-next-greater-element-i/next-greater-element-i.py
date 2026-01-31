class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Optimal- TC: O(n+m)
        hashmp = {n:i for i, n in enumerate(nums1)}
        res = [-1]*len(nums1)

        st = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while st and cur>st[-1]:
                val = st.pop()
                idx = hashmp[val]
                res[idx] = cur
            if cur in hashmp:
                st.append(cur)
        return res
        '''
        #Brute- TC: O(n*m)
        hashmp = {n:i for i, n in enumerate(nums1)}
        res = [-1]*len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in hashmp:
                continue
            for j in range(i, len(nums2)):
                if nums2[j]>nums2[i]:
                    idx = hashmp[nums2[i]]
                    res[idx] = nums2[j]
                    break
        
        return res
        '''

