__author__ = 'Hk4Fun'
__date__ = '2018/8/12 20:03'

from abc import abstractmethod


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


class WQuickUnion(QuickUnion):  # WeightedQuickUnion(加权QuickUnion)
    def __init__(self, n):
        super().__init__(n)
        self.size = [1] * n  # 记录每棵子树的大小

    def union(self, p, q):
        pid, qid = self.find(p), self.find(q)
        if pid == qid: return
        # 将小树的根节点连接到大树的根节点
        if self.size[pid] < self.size[qid]:
            self.id[pid] = qid
        else:
            self.id[qid] = pid
        self.n -= 1


class WQuickUnionWithPC(WQuickUnion):
    # WeightedQuickUnionWithPathCompression(路径压缩的加权QuickUnion)
    def find(self, p):
        root = p
        while root != self.id[root]:
            root = self.id[root]
        while p != root:  # 将寻找root路径上的结点都摘下来并连接到root上
            self.id[p], p = root, self.id[p]
        return root


if __name__ == '__main__':
    testfile = ('test/tinyUF.txt', 'test/mediumUF.txt')
    for file in testfile:
        print('test for {}'.format(file))
        with open(file, 'r') as fp:
            n = int(fp.readline())
            UF = QuickFind(n), QuickUnion(n), WQuickUnion(n), WQuickUnionWithPC(n)
            for uf in UF:
                for _ in range(n):
                    uf.union(*map(int, fp.readline().split(' ')))
                print('{}: {}'.format(type(uf), uf.count()))
                fp.seek(0, 0)
                fp.readline()
