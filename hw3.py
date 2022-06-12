def compute_average_word_length(instring,unique=False):
    '''
    This function is used to compute the average length of the words in the input string (instring).
    If the unique option is True, then exclude duplicated words.
    :param instring:input string
    :param unique:If the unique option is True, then exclude duplicated words.
    :return:the average length
    '''
    assert isinstance(instring,str)

    s = instring.split()
    sum=0
    if unique==True:
        s = list(set(s))
    for i in range(len(s)):
        sum=sum+len(s[i])
    ave=sum/len(s)
    print(ave)
    return ave

compute_average_word_length('''Mary had a little lamb
its fleece was white as snow
and everywhere that Mary went
the lamb was sure to go''',)
