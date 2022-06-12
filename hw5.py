def write_columns(data,fname='file.txt'):

    '''
    This function is used to convert  floating-point values to the hundreths place.
    And generate a three columns to a comma-separated file

    :param data:must be a list
    :param fname:is a string
    :return:three columns to a comma-separated file
    '''
    assert isinstance(data,list)
    assert isinstance(fname,str)
    for i in data:
        assert isinstance(i,int) or isinstance(i,float)

    y = []
    z = []
    for i in data:
        y.append(i ** 2)
        m = (i + i ** 2) / 3
        m = round(m, 2)
        z.append(m)

    with open(fname, 'w') as f:
        for i in range(len(data)):
            f.write(str(data[i]) + "," +str(y[i])+","+str(z[i])+"\n")

    return  fname


