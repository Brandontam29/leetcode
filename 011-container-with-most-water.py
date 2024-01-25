from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        res = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
                continue

            if height[l] > height[r]:
                r -= 1
                continue

            l += 1

        return res
