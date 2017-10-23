def zero_matrix(matrix):
    zero_row = []
    zero_col = []
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
       for j in range(col):
           if matrix[i][j] == 0:
               zero_row.append(i)
               zero_col.append(j)

    for x in zero_row:
        for y in range(col):
            matrix[x][y] = 0

    for x in zero_col:
        for y in range(row):
            matrix[y][x] = 0

    return matrix


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], ' ', end='')
        print()

print_matrix(zero_matrix([[1,2,3],[4,0,6],[7,8,9]]))
