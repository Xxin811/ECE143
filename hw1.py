def is_string_integer(x):
    '''
    It is used to convert a single string character to True or False
    if that character represents a valid integer in base 10
    :param x: single string character (i.e., 'a','b','c')
    :return: True or False
    '''
    assert len(x)==1
    if x.isdigit()==0:
        return False
    else:
        return True

input1=is_string_integer('1')
input2=is_string_integer('a')
print(input1,input2)

