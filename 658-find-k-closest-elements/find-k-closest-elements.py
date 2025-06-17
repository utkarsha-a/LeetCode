class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0 
        r = len(arr)-1
        while r-l >= k:
            if x - arr[l] > arr[r] - x:
                l += 1
            else:
                r -= 1
        return arr[l : l + k]        