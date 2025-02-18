#1.sum of matrice
def diagonal_sum(matrix):
    n = len(matrix)
    primary_sum = 0
    for i in range(n):
        primary_sum += matrix[i][i]  
    
    return primary_sum
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
primary = diagonal_sum(matrix)
print("Primary diagonal sum:", primary)

#2.Add 2 matrices


def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
sum_matrix = add_matrices(matrix1, matrix2)
print("Matrix Sum:")
for row in sum_matrix:
    print(row)