import random
def get_sample(nbits=3,prob=None,n=1):
    '''
    This function is used to function to return a list n of random samples from a finite probability mass function
    defined by a dictionary with keys defined by a specified number of bits
    :param nbits:number of bits
    :param prob: probability mass function
    :param n:number of bits
    :return:a list n of random samples
    '''
    assert isinstance(nbits,int) and nbits>0
    assert isinstance(prob,dict)
    assert sum(prob.values())==1
    assert isinstance(n,int) and n>0 and n<=2**nbits
    p1=1/2**nbits
    print(p1)
    p={}
    for i in range(0,2**nbits):
        m=[]
        x=format(i, 'b')
        b=x.zfill(nbits)
        m.append(b)
        for j in m:
            p[j]=p1

    x=random.sample(list(p), n)
    print(type(x))
    return x
