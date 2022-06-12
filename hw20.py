import random
import string

def encrypt_message(message, fname):
    '''
    Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
    name of a text file source for the codebook, generate a sequence of 2-tuples that
    represents the `(line number, word number)` of each word in the message. The output is a list
    of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple.
    :param message: message to encrypt
    :type message: str
    :param fname: filename for source text
    :type fname: str
    :returns: list of 2-tuples
    '''
    assert isinstance(message,str)
    assert isinstance(fname,str)
    assert message.islower()
    file = open(fname)
    lines = file.readlines()
    n = []
    dic = {}
    for i in lines:
        i = i.lower()
        for c in string.punctuation:
            i = i.replace(c, '')
        i = i.replace('\n', '')
        n.append(i)
    for i in range(len(n)):
        l = n[i].split()
        for j in range(len(l)):
            if l[j] not in dic.keys():
                dic[l[j]] = []
            dic[l[j]].append((i + 1, j + 1))


    x = message.split()

    c = []
    for i in x:
        if i in dic.keys():
            random.shuffle(dic[i])
            val = dic[i].pop(0)
            c.append(val)

    return (c)

def decrypt_message(inlist, fname):
    '''
     Given `inlist`, which is a list of 2-tuples`fname` which is the
     name of a text file source for the codebook, return the encrypted message.

     :param message: inlist to decrypt
     :type message: list
     :param fname: filename for source text
     :type fname: str

     :returns: string decrypted message
     '''
    assert isinstance(inlist,list)
    assert isinstance(fname,str)
    assert len(inlist)==len(set(inlist))
    file = open(fname)
    lines = file.readlines()
    n = []
    m = []
    dic = {}
    for i in lines:
        i = i.lower()
        for c in string.punctuation:
            i = i.replace(c, '')
        i = i.replace('\n', '')
        n.append(i)
    for i in range(len(n)):
        l = n[i].split()
        for j in range(len(l)):
            if l[j] not in dic.keys():
                dic[l[j]] = []
            dic[l[j]].append((i + 1, j + 1))
    for i in inlist:
        for key in dic.keys():
            if i in dic[key]:
                m.append(key)

    x = ' '.join(m)

    return (x)

x1 = encrypt_message('let us not say we met late at the night about the secret','codebook.txt')
print(x1)
inlist = [(1394, 2), (1773, 11), (894, 10), (840, 1), (541, 2), (1192, 5), (1984, 7), (2112, 6), (1557, 2), (959, 8), (53, 10), (2232, 8), (552, 5)]
x2 = decrypt_message(inlist,'codebook.txt')
print (x2)


