def map_bitstring(x):
    '''
    This function is used to takes a list of bitstrings (i.e., 0101) and maps each bitstring to 0
    if the number of 0s in the bitstring strictly exceeds the number of 1s.
    :param x:a list of bitstrings
    :return:a dictionary
    '''
    assert isinstance(x,list)
    for i in x:
        for j in i:
            assert isinstance(j,str)
            assert int(j)==0 or int(j)==1

    c=[]
    for i in range(len(x)):
        if sum(int(j)==0 for j in x[i])>sum(int(j)==1 for j in x[i]):
            c.append(0)
        else:c.append(1)
    return dict(zip(x,c))

