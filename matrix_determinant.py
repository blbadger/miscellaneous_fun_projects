# matrix_determinant.py

# standard library
import copy
matrix_dictionary = {}

def determinant(matrix, matrix_dictionary):
    ''' Returns the determinant of a matrix of arbirtary size 
    (note that only nxn matricies have determinants).  Takes
    one argument, a list of lists corresponding to an array
    with numerical values (float or int) for the matrix of interest
    '''
    # base case #1: if the matrix is 1x1
    if len(matrix) == 1: 
        return matrix[0][0]

    # base case #2: if the matrix is 2x2
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # iterate through the values of the matrix, removing the row and 
    # col of each value contributing to the determinant. Find the 
    # value recursively, and sum to return the determinant
    else:
        result = 0
        for i in range(len(matrix)):
            new_matrix = [matrix[j] for j in range(len(matrix)) if j != 0]
            new_matrix2 = copy.deepcopy(new_matrix)
            
            for row in new_matrix2:
                del row[i]

            new_tuple = tuple(tuple(i) for i in new_matrix2)
            if i % 2 == 0:
                if new_tuple not in matrix_dictionary:
                    new_matrix_det = determinant(new_matrix2, matrix_dictionary)
                    result += matrix[0][i] * new_matrix_det
                    matrix_dictionary[new_tuple] = new_matrix_det
                else:
                    result += matrix[0][i] * matrix_dictionary[new_tuple]
            else:
                if new_tuple not in matrix_dictionary:
                    new_matrix_det = determinant(new_matrix2, matrix_dictionary)
                    matrix_dictionary[new_tuple] = new_matrix_det
                    result -= matrix[0][i] * new_matrix_det
                else:
                    result -= matrix[0][i] * matrix_dictionary[new_tuple]


    return result


# example input
matrix = [
[1, 2, 1, 4, 3, -1, 4, 1], 
[1, 2, 3, 2, 9, 1, 10, 2], 
[1, 2, 1, 1, 9, 0, 15, 3], 
[8, 0, 1, 0, 2, 3, 4, -8], 
[2, 3, 4, 0, 1, 2, -1, 3], 
[2, 1, 0, 0, 1, 1, -5, -6], 
[5, -6, 3, 7, -4, 0, 0, 1],
[1, 3, -5, 1, 7, 0, 4, -1]
]

matrix2 = [[1,2,3],[4,5,6],[7,8,9]]

# example function call
print (determinant(matrix, matrix_dictionary))