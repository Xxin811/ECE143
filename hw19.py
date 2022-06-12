import os
def split_by_n(fname,n=3):
    '''
    Split files into sub files of near same size
    fname : Input file name
    n is the number of segments
    '''
    assert isinstance(n,int) and n > 0
    assert isinstance(fname,str)

    combstr = ""
    count = 0
    i = 0
    fsize = os.path.getsize(fname)
    fp = open(fname, 'r')
    lines = fp.readlines()
    for i in range(len(lines)):
        combstr = combstr + ''.join(lines[i]).lstrip('')
        if (len(combstr) > fsize // n - len(lines[i])) and count < n-1:
            tempLog = open(fname + "_" + str(count).zfill(3) + ".txt", 'wt')
            tempLog.write(combstr)
            tempLog.close()
            combstr = ""
            i += 1
            count += 1

        elif count == n - 1:

            tempLog = open(fname + "_" + str(count).zfill(3) + ".txt", "wt")
            tempLog.write(combstr)
            tempLog.close()
        fp.close()
# split_by_n('pg5200.txt',8)
# n = 8
# for i in range(n):
#     fsize2 = os.path.getsize('pg5200.txt' + "_" + str(i).zfill(3) + ".txt")
#     print(fsize2)
