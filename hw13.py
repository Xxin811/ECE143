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
def gather_values(x):
    '''

    :param x: a list of binary number
    :return: a new dictionary
    '''
    assert isinstance(x,list)
    for i in x:
        assert isinstance(i,str)
    p=[]
    y = list(map_bitstring(x).keys())
    n = list(map_bitstring(x).values())

    a = {}
    for j in x:
        if x.count(j) > 1:
            a[j] = x.count(j)
    for i in range(len(n)):
        m=list(a.values())
        p.append(m[i]*[n[i]])

    p = dict(zip(y,p))
    print(p)

    return p


# x=gather_values( ['10', '11', '01', '00', '10', '00', '00', '11', '10', '00', '00', '01', '01', '11', '10', '00', '11', '10', '11', '11'])