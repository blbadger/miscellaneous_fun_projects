# standard library
import copy

def determinant(matrix):
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

            if i%2 == 0:
                result += matrix[0][i] * determinant(new_matrix2)
            else:
                result -= matrix[0][i] * determinant(new_matrix2)

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

# example function call
print (determinant(matrix))