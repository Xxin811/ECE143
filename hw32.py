import numpy as np
from collections import defaultdict
def find_convex_cover(pvertices,clist):
    '''

    :param pvertices:(n-1) long iterable of polygon vertices
    :param clist: tuples of (n-1) circle-centers
    :return:long m long list of radii, ri corresponding to the m circle-centers
    '''
    assert isinstance(clist, list)
    assert isinstance(pvertices, np.ndarray)
    for m in clist:
        assert isinstance(m, tuple)
    dis = []
    dis_sqr = []
    min_dis_sqr = []
    for p in pvertices:
        dis.append(p-clist)
    for a in dis:
        for i in range(len(a)):
            # x = a[i][0]**2+a[i][1]**2
            x = [((a[i][0]) ** 2 + (a[i][1]) ** 2) for i in range(len(a))]
            dis_sqr.append(x)
            min_dis_sqr.append(x.index(min(x)))
    dic_center = defaultdict(list)
    for i in range(len(min_dis_sqr)):
        dic_center[min_dis_sqr[i]].append(i)

    r = [0] * len(clist)
    for key, values in dic_center.items():
        radius = -1
        for j in values:
            radius = max(radius, dis_sqr[j][key])
        # print(radius)
        r[key] = np.sqrt(radius)
    return r


# pvertices = np.array([[ 0.573,  0.797],
#                         [ 0.688,  0.402],
#                         [ 0.747,  0.238],
#                         [ 0.802,  0.426],
#                         [ 0.757,  0.796],
#                         [ 0.589,  0.811]])
# clist = [(0.7490863467660889, 0.4917635308023209),
#               (0.6814339441396109, 0.6199470305156477),
#               (0.7241617773773865, 0.6982813914515696),
#               (0.6600700275207232, 0.7516911829987891),
#               (0.6315848053622062, 0.7730550996176769),
#               (0.7348437356868305, 0.41342916986639894),
#               (0.7597683050755328, 0.31729154508140384)]
# print(find_convex_cover(pvertices,clist))
