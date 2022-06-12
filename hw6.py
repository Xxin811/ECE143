def write_chunks_of_five(words,fname='file2.txt'):
    '''
    This function is used to create a new file that consists of each consecutive non-overlapping sequence of
    five lines merged into one line by using the corpus of 10,000 common english words
    :param words:a list of words from the 10000 common English words
    :param fname:output filename string
    :return:the new file
    '''
    assert isinstance(words,list)
    assert isinstance(fname,str)

    l = len(words) // 5
    r = len(words) % 5

    if r==0:
        with open(fname, 'w') as f:
            for i in range(0, l*5, 5):
                f.write(str(words[i]) + ' ' + str(words[i + 1]) + ' ' + str(words[i + 2]) + ' ' + str(words[i + 3]) + ' ' + str(words[i + 4]) + "\n")
        f.close()
    else:
        with open(fname, 'w') as f:
            for i in range(0,l*5,5):
                f.write(str(words[i]) + ' ' + str(words[i+1])+' '+ str(words[i+2])+' '+ str(words[i+3])+' '+ str(words[i+4])+"\n")

            for j in range(r):
                f.write(str(words[5 * l + j]) + ' ')
        f.close()

    return  fname

