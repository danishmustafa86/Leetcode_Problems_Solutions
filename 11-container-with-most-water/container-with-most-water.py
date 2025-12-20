class Solution:
    def maxArea(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        maxArea = 0
        while l < r:
            minvalue = min(height[l], height[r])
            difference = r - l
            curArea = minvalue * difference
            maxArea = max(curArea , maxArea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea






























        # l, r = 0, len(height) - 1
        # maxarea = 0
        # while l < r:
        #     curarea = min(height[l] , height[r]) * (r - l )
        #     maxarea = max( curarea, maxarea)
        #     if height[l] < height[r]:
        #         l += 1
        #     else:
        #         r -= 1
        # return maxarea
