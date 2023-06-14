#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    temp = 0

    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            temp = matrix[i][j] ** 2
            new_matrix[i].append(temp)

    return new_matrix
