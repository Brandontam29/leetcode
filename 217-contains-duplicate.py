from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    s = set()
    for n in nums:
        if n in s:
            return True

        s.add(n)

    return False
