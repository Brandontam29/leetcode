from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            target = 0 - a
            l = i + 1
            r = len(nums) - 1

            while l < r:
                b = nums[l]
                c = nums[r]

                if b + c < target:
                    while l < r and nums[l] == b:
                        l += 1
                    continue

                if b + c > target:
                    while l < r and nums[r] == c:
                        r -= 1
                    continue

                res.append([a, b, c])
                while l < r and nums[l] == b:
                    l += 1

        return res
