from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    d = {}
    for n in nums:
        if not n in d:
            d[n] = 0
        else:
            d[n] += 1

    ds = sorted(d, key=d.get, reverse=True)

    return ds[0:k]


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
# Doesn't have to work with strings but it does
print(topKFrequent([1, "a", 2, 3, 4, 6, 1, 2, 4, 2, 6, 7, 2, 4, "a", "s",
      "d", "f", "d", "x", "s", "a", "f", "s", "d", "f", 's', "d", "f", 'd', 1, 2, 3, 5, 5, 6, 7, 8, 3, 4, 5, 3, 1, 3, 5, 6, 8, 9, 3, 3, 5, 3, 2, 3, 1, 3, 2, 3, 1, 4, 5, 45, 4, 45, 5, 5, "o", 55, 5, 5, 55, 5, 5, 5, 5, 5, 5, 5, 5, 56, 6, 7, 4, 3, 25, 234, ], 5))
