import numpy as np
from matplotlib.pylab import subplots, cm
import matplotlib.pylab as plt


def gen_rand_slash(m = 6,n = 6,direction = 'back'):
    '''
    This function is used to function that can produce a uniformly random forward or backslashed
    image (i.e., Numpy array) of at least two non-zero pixels.
    :param m: The number of rows in the image.
    :param n: The number of columns in the image.
    :param direction: Determine which side the slash is biased to.
    :return: A numpy array
    '''
    assert isinstance(m,int)
    assert isinstance(n,int)
    assert direction=='back' or direction=='forward'
    c=np.zeros((m,n),dtype=int)
    if direction=='back':
        row=np.random.randint(0,m-1)
        col=np.random.randint(0,n-1)
        max=np.min((m-row,n-col))
        length = np.random.randint(2, max + 1)
        for i in range(0,length):
            c[row+i][col+i]=1

    elif direction=='forward':
        row=np.random.randint(1,m)
        col=np.random.randint(0,n-1)
        max = np.min((row+1, n-col))
        length = np.random.randint(2, max+1)
        for i in range(0,length):
            c[row-i][col+i]=1
    return c


x = gen_rand_slash(m=6,n=6,direction='back')
fig,axs=subplots(3,3,sharex=True,sharey=True)
for ax in axs.flatten():
    ax.imshow(gen_rand_slash(),cmap=cm.gray_r)
plt.show()
