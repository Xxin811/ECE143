def get_power_of3(x):
    '''
    This function is used to construct any number between 1 and 40
    by using the set of of weights {1,3,9,27} with the addition and subtraction operation
    :param x: input number
    :return: {x1,x2,x3,x4} representing the weighting of {1,3,9,27}
    '''
    assert isinstance(x,int)
    assert x in range(0,41)
    w=(-1,0,1)

    for x1 in w:
        for x2 in w:
            for x3 in w:
                for x4 in w:
                    if x1*1+x2*3+x3*9+x4*27==x:
                        return [x1, x2, x3, x4]




