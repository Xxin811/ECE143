import random
def multinomial_sample(n, p, k=1):
    '''
    Return samples from a multinomial distribution.

    n:= number of trials
    p:= list of probabilities
    k:= number of desired samples
    '''
    assert isinstance(n,int)
    assert sum(p)==1
    for i in p:
        assert i>=0 and i<1
    assert isinstance(k,int)
    assert isinstance(p,list)

    num_output = []
    size = len(p)
    lst = list(range(size))
    for i in range(k):
        results = [0] * size
        record = []
        for j in range(n):
            idx = random.choices(lst, p)[0]
            record.append(idx)
        for m in record:
            results[m] += 1

        num_output.append(results)
    return num_output


print(multinomial_sample(10, [1 / 3, 1 / 3, 1 / 3], k=10)) #as a test