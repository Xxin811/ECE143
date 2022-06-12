def get_trapped_water(seq) :
    '''
    This function is used to Compute how many units of water remain trapped between the walls in the map
    :param seq:an input list
    :return:units of water remain trapped between the walls in the map
    '''
    assert isinstance(seq,list)
    for i in seq:
        assert isinstance(i,int) and i >= 0
    assert len(seq) >= 3
    vol = 0
    max_l = [0] * len(seq)
    max_r = [0] * len(seq)
    max_l[0] = seq[0]

    for j in range(1, len(seq)):
        max_l[j] = max(seq[j], max_l[j-1])

    max_r[len(seq)-1] = seq[-1]

    for m in range(len(seq)-2, -1, -1):
        max_r[m] = max(seq[m], max_r[m+1])

    for s in range(1, len(seq)-1):
        # print(s)
        vol += min(max_l[s], max_r[s]) - seq[s]
        # print(vol)
    return vol



# print(get_trapped_water([4,2,0,3,2,5]))