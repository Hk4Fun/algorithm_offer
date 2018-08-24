__author__ = 'Hk4Fun'
__date__ = '2018/8/24 3:38'


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def treePrint(root):
    treeList = serialize(root)
    levels = len(treeList)
    start = [(2 ** i - 1) for i in range(levels, 0, -1)]
    middle = [start[-1]] + start[:-1]
    for i in range(levels):
        print(' ' * start[i], end='')
        for v in treeList[i]:
            if v is None:
                print(' ' * (middle[i] + 1), end='')
            else:
                print(v, ' ' * middle[i], end='')
        print('')


def serialize(root):
    level, res = [root], []
    while level:
        res.append([])
        next_level = []
        for cur in level:
            if cur:
                res[-1].append(cur.val)
                next_level += (cur.left, cur.right)
            else:
                res[-1].append(None)
        level = next_level
    return res[:-1]


if __name__ == '__main__':
    #        8
    #    6         10
    # 5    7          11
    # 1  2
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node5 = TreeNode(5, node1, node2)
    node7 = TreeNode(7)
    node6 = TreeNode(6, node5, node7)
    node11 = TreeNode(11)
    node10 = TreeNode(10, None, node11)
    node8 = TreeNode(8, node6, node10)
    treePrint(node8)
    print('* ' * 20)
    treePrint(node5)
    print('* ' * 20)
    treePrint(node6)
    print('* ' * 20)
    treePrint(node7)
    print('* ' * 20)
    treePrint(node10)
