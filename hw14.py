def threshold_values(seq,threshold=1):
    '''
    :param seq: Input sequence
    :param threshold: pick up the most frequent values
    :return: a dictionary
    '''
    assert isinstance(seq,list)

    b = {}
    for j in seq:
        if seq.count(j) > 1:
            b[j] = seq.count(j)


    a_order = dict(sorted(b.items(), key=lambda item: item[1], reverse=True))

    counter = 0

    for key in a_order.keys():
        if counter < threshold:
            a_order[key] = 1
            counter += 1
        else:
            a_order[key] = 0
    print(a_order)
    return a_order
seq= ['1111', '0110', '1001', '0011', '0111', '0100', '0111', '1100', '0011', '0010', '0010', '1010', '1010', '1100', '0110', '0101', '0110', '1111', '1001', '0110', '0010', '1101', '0101', '0010', '0100', '0010', '0000', '0000', '0011', '0110', '0101', '1010', '1011', '1101', '1100', '0111', '1110', '0100', '0110', '1101', '0001', '1110', '0010', '0001', '1010', '1010', '0011', '1000', '0010', '0000', '1010', '1101', '1111', '1000', '1000', '0010', '1010', '0101', '0101', '1101', '0110', '1001', '1100', '1100', '1000', '1010', '0011', '0101', '0101', '0011', '0001', '1010', '0011', '0011', '1101', '1010', '0101', '0011', '1011', '0101', '0000', '1111', '1001', '0101', '1100', '0011', '1111', '1101', '0001', '1111', '1110', '1111', '0001', '0010', '0110', '0100', '0101', '1100', '1110', '1001']
x=threshold_values(seq,1)