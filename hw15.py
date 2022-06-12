import itertools
def descrambler(w,k):
    '''
    This function is used to generate the  a sequence of n lower-case letters
    and a k-tuple of integers that indicate partition-lengths of the sequence.

    :param w: a string of words
    :param k:a phrase of k words
    :return:iteratively yield the output
    '''
    assert isinstance(w,str)
    assert isinstance(k,tuple)
    assert len(w)>0 and len(k>0)
    assert sum(k)==len(w)
    for i in k:
        assert isinstance(i,int) and i>0

    words = open("google-10000-english-no-swears.txt", "r")
    word_list = [line.strip() for line in words.readlines()]
    m=[]
    for i in word_list:
        a=len(i)
        if a not in m:
            m.append(a)
    m = sorted(m)
    w_dict = {}
    for i in range(1, max(m) + 1):
        w_dict['len' + str(i)] = {s for s in word_list if len(s) == i}




    return




