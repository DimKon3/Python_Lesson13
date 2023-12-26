import random

def rand_matrix():
    matrix = []
    for __ in range(X):
        row = []
        for __ in range(Y):
            row.append(random.randint(0, 99))
        matrix.append(row)
    return matrix

def list_out(lst):
    for val in lst:
        print(f'{val:4}', end='')
    print()

def matrix_out(matrix):
    for row in matrix:
        list_out(row)
    print()

X, Y = map(int,input("Введите размерность матрицы через пробел ").split())

matrix_1 = rand_matrix()
matrix_2 = rand_matrix()
matrix_3 = rand_matrix()

matrix_out(matrix_1)
matrix_out(matrix_2)

for i in range(X):
    for j in range(Y):
        matrix_3[i][j]  = matrix_1[i][j] + matrix_2[i][j]

matrix_out(matrix_3)
