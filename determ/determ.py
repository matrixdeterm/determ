def determ(matrix, n):
    """"
    match n:
        case 1:
            return matrix[0][0]
        case 2:
            return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        case n:
            result = 0
            for i in range(n):
                matrix_n = []
                for k in range(n):
                    s = []
                    for j in range(n):
                        if k != 0 and j != i:
                            s += [matrix[k][j]]
                    if s != []:
                        matrix_n += [s]
                result += matrix[0][i] * determ(matrix_n, n - 1) * (-1) **i
            return result
            """

#matrix = [[1, 2, 9, 3], [3, 7, -1, 5], [5, 3, 1, 7], [1, 2, 5, 6]]
#print(determ(matrix, len(matrix)))



