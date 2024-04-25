#!/usr/bin/python3

'''0. Rotate 2D Matrix.
'''



def rotate_2d_matrix(matrix):
    '''Rotates an m by n 2D matrix by moving th first
    column element to the first row, second to the second
    row....
    '''
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    m_rows = len(matrix)
    m_cols = len(matrix[0])
    if not all(map(lambda num: len(num) == m_cols, matrix)):
        return
    col, rol = 0, m_rows - 1
    for x in range(m_cols * m_rows):
        if x % m_rows == 0:
            matrix.append([])
        if rol == -1:
            rol = m_rows - 1
            col += 1
        matrix[-1].append(matrix[rol][col])
        if col == m_cols - 1 and rol >= -1:
            matrix.pop(rol)
        rol -= 1
