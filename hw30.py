def next_permutation(t):
    '''
    this funcion is used to permutation of any length, generate the next permutation in lexicographic order
    :param t:tuple
    :return:tuple
    '''
    assert isinstance(t, tuple)
    assert all(i == x for i, x in enumerate(sorted(t)))
    for i in t:
        assert isinstance(i, int) and 0 <= i <= len(t)

    t = list(t)
    i = len(t) - 2
    while i >= 0 and t[i] >= t[i+1]:
        i = i - 1
    if i >= 0:
        j = len(t) - 1
        while j >= 0 and t[j] <= t[i]:
            j = j - 1
        t[i], t[j] = t[j], t[i]
    reverse(t, i + 1)
    return tuple(t)

def reverse(t,idx):
    i = idx
    j = len(t) - 1
    while i < j:
        t[i],t[j] = t[j],t[i]
        i = i + 1
        j = j - 1
    return t

# print(next_permutation((2,3,1)))
