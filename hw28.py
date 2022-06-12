def count_paths(m,n,blocks):
    '''
    # denotes a blockage and . denotes a passable opening
    :param m:horizontal rows
    :param n:vertical columns
    :param blocks:The blocks variable is a list of tuples indicating the blocked # entries in the grid
    :return:the number of connected paths
    '''
    assert isinstance(m,int) and m > 0
    assert isinstance(n,int) and n > 0
    for i in blocks:
        assert isinstance(i, tuple)
        assert 0 <= i[0] < m
        assert 0 <= i[1] < n
        assert len(i) == 2
    mat = [[0] * n] * m
    mat[0][0] = 1
    for row in range(m):
        for col in range(n):
            if (row,col) in blocks:
                mat[row][col] = 0
            elif row != 0 and col== 0:
                mat[row][col] = mat[row - 1][col]
            elif row == 0 and col!= 0:
                mat[row][col] = mat[row][col - 1]
            else:
                mat[row][col]=mat[row][col-1]+mat[row-1][col]
    return mat[m-1][n-1]
# print(count_paths(3,4,[(0,3),(1,1)]))


