import types
def tracker(p, limit):
    '''

    :param p: generator
    :param limit: positive int
    Yield
    '''

    assert isinstance(p, types.GeneratorType)
    assert isinstance(limit, int)
    assert limit > 0

    count = 0  # number of odd second that iterated

    while count < limit:

        a = next(p).seconds
        if (a % 2) == 1:
            count += 1
        nlt = yield count
        if nlt != None:
            limit = nlt

