class Node:
    def __init__(self, val:int=0, left=None, right=None):
        assert isinstance(left,Node) or left is None
        assert isinstance(right,Node) or right is None
        self.val = val
        self.left = left
        self.right = right

class Tree(object):
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, val):
        self.add(self.root, val)

    def add(self, node, val):
        if node.val == val:
            return
        else:
            if val < node.val:
                if node.left == None:
                    node.left = Node(val)
                else:
                    self.add(node.left, val)
            else:
                if node.right == None:
                    node.right = Node(val)
                else:
                    self.add(node.right, val)


    def get_parent(self, val):
        if self.root.val == val:
            return val
        curr = self.root
        while curr != None:
            if val < curr.val:
                if curr.left and curr.left.val == val:
                    return curr.val
                else:
                    curr = curr.left
            elif val > curr.val:
                if curr.right and curr.right.val == val:
                    return curr.val
                else:
                    curr = curr.right



def get_tree_list(p):
    '''

    :param p:
    :return:
    '''
    assert isinstance(p,list)
    assert len(p) == len(set(p))
    for i in p:
        assert isinstance(i,int)
    tree=Tree(p[0])
    output=[]
    for i in p[1:]:
        tree.insert(i)
    for j in range(len(p)):
        m = tree.get_parent(j)
        output.append(m)
    return output

p = [8, 5, 1, 10, 0, 4, 2, 3, 7, 9, 6]
print(get_tree_list(p))