def convert_hex_to_RGB(hex_num):
    '''
    It is used to convert a list of color hex-codes into a list of RGB-tuples
    :param x: A list of color hex-codes
    (e.g., ['#FFAABB'])
    :return:A list of RGB-tuples.
    (e.g., [(255,170,187)] corresponds to the example)
    '''

    assert isinstance(hex_num,list)
    rgb=[]
    for i in range(len(hex_num)):
        assert len(hex_num[i]) == 7
        r = int(hex_num[i][1:3],16)
        g = int(hex_num[i][3:5],16)
        b = int(hex_num[i][5:7],16)
        rgb_temp = (r, g, b)
        rgb.append(rgb_temp)
    print(rgb)

    return rgb
convert_hex_to_RGB(['#FFAABB','#AAAAAA'])
