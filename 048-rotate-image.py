# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2:


# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

# TODO:  THIS IS WRONG
from typing import List


def rotate(matrix: List[List[int]]) -> None:
    l, r = 0, len(matrix) - 1

    while l < r:
        for i in range(r-l):
            t, b = l, r
            topLeft = matrix[t][l + i]
            matrix[t][l + i] = matrix[b][l+i]
            matrix[b][l+i] = matrix[b - i][r]
            matrix[b-i][r] = matrix[t][r-i]
            matrix[t][r-i] = topLeft

        l += 1
        r -= 1


matrix3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix3)
print(matrix3)  # [[7,4,1],[8,5,2],[9,6,3]]

matrix4 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
rotate(matrix4)
print(matrix4)  # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
