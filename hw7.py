def slide_window(x,width,increment):
    '''
    This function is used to a sequence of overlapping lists. And it take the window width and the window increment as inputs.
    and it should produce a sequence of overlapping lists from the input list.
    In addition,In the event that the input parameters do not yield a complete set of even sublists, just truncate the ragged tail.
    :param x:an arbitrary input list
    :param width:window width
    :param increment:window increment
    :return:a sequence of overlapping lists
    '''
    assert isinstance(x,list)
    assert isinstance(width,int) and width>0
    assert isinstance(increment,int) and increment>0
    w = len(x)
    r = w % increment
    z=[]

    for i in range(0,w-width+r,increment):
        y=[]
        for j in range(i,i+width):
            y.append(x[j])
        z.append(y)
    print(z)

    return z
