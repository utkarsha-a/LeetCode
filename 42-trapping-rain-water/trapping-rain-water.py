class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        l = 0
        r = len(height)-1
        maxL = height[l]
        maxR = height[r]
        water_trapped = 0

        while l<r:
            if maxL <= maxR:
                l += 1
                maxL = max(maxL, height[l])
                water_trapped += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                water_trapped += maxR - height[r]
        return water_trapped