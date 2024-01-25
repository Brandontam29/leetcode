from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lower = 0
        upper = len(numbers) - 1

        while lower != upper:
            if numbers[lower] + numbers[upper] == target:
                return [lower + 1, upper + 1]

            if numbers[lower] + numbers[upper] < target:
                lower += 1

            if numbers[lower] + numbers[upper] > target:
                upper -= 1
