__author__ = 'Hk4Fun'
__date__ = '2018/8/12 20:03'

from abc import abstractmethod

'''
优化后的并查集（路径压缩的加权QuickUnion）其时间复杂度为 O(log*n)  
log*n = 0 if n <= 1 else 1 + log*n  (递归定义)
其复杂度低于logn，近乎是O(1)级别的
'''

class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n  # 分量个数，一开始每个触点还没相连，各自形成分量
        self.id = list(range(n))  # 分量id（以触点作为索引），一开始所有触点的代表id都是自己

    def count(self):
        """
        返回连通分量的个数
        """
        return self.n

    def connected(self, p: int, q: int) -> bool:
        """
        判断p和q是否相连
        """
        return self.find(p) == self.find(q)

    @abstractmethod
    def find(self, p: int) -> bool:
        """
        返回p的根节点（代表结点id）
        """
        pass

    @abstractmethod
    def union(self, p: int, q: int) -> None:
        """
        连接p和q
        """
        pass


class QuickFind(UnionFind):
    def find(self, p):
        return self.id[p]

    def union(self, p, q):
        pid, qid = self.find(p), self.find(q)
        if pid == qid: return
        # 遍历整个数组，将所有和id[p]相等的元素的值变为id[q]的值，反之亦可
        for i, v in enumerate(self.id):
            if v == pid: self.id[i] = qid
        self.n -= 1


class QuickUnion(UnionFind):
    def find(self, p):
        while self.id[p] != p:  # 向上一直找到p的根节点
            p = self.id[p]
        return p

    def union(self, p, q):
        pid, qid = self.find(p), self.find(q)
        if pid == qid: return
        self.id[pid] = qid  # 将p的根结点连接到q的根结点，反之亦可
        self.n -= 1


class WQuickUnion(QuickUnion):  # WeightedQuickUnion(加权QuickUnion)，基于树的结点个数
    def __init__(self, n):
        super().__init__(n)
        self.size = [1] * n  # 记录每棵子树的大小

    def union(self, p, q):
        pid, qid = self.find(p), self.find(q)
        if pid == qid: return
        # 将小树的根节点连接到大树的根节点
        if self.size[pid] < self.size[qid]:
            self.id[pid] = qid
            self.size[qid] += self.size[pid]
        else:
            self.id[qid] = pid
            self.size[pid] += self.size[qid]
        self.n -= 1


class DQuickUnion(QuickUnion):
    # 基于depth(rank)的优化，depth[i]表示根节点为i的树的高度
    # 有时候结点数多的数可能深度更小，因此考虑把深度小的树连接到深度大的树
    def __init__(self, n):
        super().__init__(n)
        self.depth = [1] * n  # 记录每棵子树的深度

    def union(self, p, q):
        pid, qid = self.find(p), self.find(q)
        if pid == qid: return
        # 将深度小的树的根节点连接到深度大的树的根节点
        # 当一个深度比另一个大是，连接后深度大的树其深度不会改变
        # 但如果两个深度一样，则连接后深度+1
        if self.depth[pid] < self.depth[qid]:
            self.id[pid] = qid
        elif self.depth[qid] > self.depth[pid]:
            self.id[qid] = pid
        else:
            self.id[qid] = pid
            self.depth[pid] += 1
        self.n -= 1


class WQuickUnionWithPC(WQuickUnion):
    # WeightedQuickUnionWithPathCompression(路径压缩的加权QuickUnion)
    def find(self, p):  # 非递归实现
        root = p
        while root != self.id[root]:
            root = self.id[root]
        while p != root:  # 将寻找root路径上的结点都摘下来并连接到root上
            self.id[p], p = root, self.id[p]
        return root

    def find_recursive(self, p):  # 递归实现，代码简洁
        if self.id[p] != p:
            self.id[p] = self.find_recursive(self.id[p])  # 向上递归一直找到p的根节点
        return self.id[p]  # 一路返回根节点


class DQuickUnionWithPC(DQuickUnion):
    # 基于depth优化的路径压缩QuickUnion
    # 另一种压缩方式，只是单次find压缩不能保证连接到根节点
    # 多次调用后可以连接到根节点
    def find(self, p):
        while self.id[p] != p:
            # 注意到这里改变了树的深度却没有对depth进行维护，因为这样会降低find的性能
            # 而实际上不对其进行维护也不会影响union，因为此时的depth实际上表示树的排名权重
            self.id[p] = self.id[self.id[p]]  # 连接到父结点的父结点
            p = self.id[p]
        return p


if __name__ == '__main__':
    testfile = ('test/tinyUF.txt', 'test/mediumUF.txt')
    for file in testfile:
        print('test for {}'.format(file))
        with open(file, 'r') as fp:
            n = int(fp.readline())
            UF = QuickFind(n), QuickUnion(n), WQuickUnion(n), DQuickUnion(n), \
                 WQuickUnionWithPC(n), DQuickUnionWithPC(n),
            for uf in UF:
                for _ in range(n):
                    uf.union(*map(int, fp.readline().split(' ')))
                print('{}: {}'.format(type(uf), uf.count()))
                fp.seek(0, 0)
                fp.readline()
