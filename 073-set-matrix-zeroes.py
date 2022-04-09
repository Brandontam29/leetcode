from typing import List


# iterative solution O(2n^2)
def setZeroes(matrix: List[List[int]]) -> None:
    def findZeroes(matrix: List[List[int]]):
        dict = {"row": [], "col": []}
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    dict["row"].append(row)
                    dict["col"].append(col)

        return dict

    zeroes = findZeroes(matrix)

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if r in zeroes["row"] or c in zeroes["col"]:
                matrix[r][c] = 0


# O(1) space complexity
def setZeroes2(matrix: List[List[int]]) -> None:
    ROWS, COLS = len(matrix), len(matrix[0])

    r1 = False

    for r in range(ROWS):
        for c in range(COLS):

            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    r1 = True

    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0

    if r1:
        for c in range(COLS):
            matrix[0][c] = 0


matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
setZeroes2(matrix1)
print(matrix1)
# [[1,0,1],[0,0,0],[1,0,1]]

matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
setZeroes2(matrix2)
print(matrix2)
# [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
