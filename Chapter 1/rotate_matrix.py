def rotate_matrix_clockwise(matrix):
    n = len(matrix)
    for x in range(n // 2):
        for y in range(x, n - x - 1):
            # save top
            temp = matrix[x][y]
            # left -> top
            matrix[x][y] = matrix[-y-1][x]
            # bottom -> left
            matrix[-y-1][x] = matrix[-x-1][-y-1]
            # right -> bottom
            matrix[-x-1][-y-1] = matrix[y][-x-1]
            # top -> right
            matrix[y][-x-1] = temp

    return matrix


# def rotate_matrix_counterclockwise(matrix):
#     n = len(matrix)
#     for x in range(n // 2):
#         for y in range(x, n - x - 1):
#             temp = matrix[x][y]
#             # right -> top
#             matrix[x][y] = matrix[y][-x-1]
#             # bottom -> right
#             matrix[y][-x-1] = matrix[-x-1][-y-1]
#             # left -> bottom
#             matrix[-x-1][-y-1] = matrix[-y-1][x]
#             # top -> left
#             matrix[-y-1][x] = temp
#
#     return matrix


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], ' ', end='')
        print()


# print_matrix(rotate_matrix_counterclockwise([[1,2],[3,4]]))
print_matrix(rotate_matrix_counterclockwise([[1,2,3],[4,5,6],[7,8,9]]))
# print_matrix(rotate_matrix_clockwise([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]))
