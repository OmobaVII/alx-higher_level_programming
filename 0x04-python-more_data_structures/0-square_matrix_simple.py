def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(lambda i : i ** 2, i)))
    return (new_matrix)