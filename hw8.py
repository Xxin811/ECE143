def fibonacci(n):
    '''
    This function is a generator to compute the first n Fibonacci numbers.
    :param n:Number of the first n Fibonacci numbers
    :return:a list of fibonacci numbers
    '''
    assert isinstance(n,int) and n>=2


    one = 1
    two = 1
    for i in range(n):
        yield one
        one, two = two, one + two
        i += 1
A=[]
for i in fibonacci(10):
    A.append(i)
print(A)