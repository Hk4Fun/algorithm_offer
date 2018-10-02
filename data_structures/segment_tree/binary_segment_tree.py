__author__ = 'Hk4Fun'
__date__ = '2018/10/2 10:34'

'''
使用二叉树实现，代码简洁
'''


class Node:
    def __init__(self, start, end):
        self.start = start  # 区间左边界
        self.end = end  # 区间右边界
        self.merge_val = 0  # 区间统计值，有merger确定其合并逻辑
        self.left = self.right = None  # 左右孩子结点

    def __repr__(self):
        return 'Node(start={}, end={}), merge_val={!r}'.format(self.start, self.end, self.merge_val)


class SegmentTree:
    def __init__(self, arr, merger):
        self._data = list(arr)
        self._merger = merger
        self._root = self._build_tree(0, self.size - 1)

    def __repr__(self):
        return 'SegmentTree([{}])'.format(','.join(str(val) for val in self._level_order()))

    def __setitem__(self, idx, val):
        if not 0 <= idx < self.size:
            raise IndexError('invalid index')
        self._data[idx] = val  # 更新原始数据
        self._update(self._root, idx, val)

    def __getitem__(self, idx):
        if not 0 <= idx < self.size:
            raise IndexError('invalid index')
        return self._data[idx]

    @property
    def size(self):
        """返回原始数组的元素个数"""
        return len(self._data)

    def query(self, l, r):
        if not 0 <= l <= r < self.size:
            raise IndexError('invalid query index')
        return self._query(self._root, l, r)

    def _build_tree(self, l, r):
        """递归构造线段树，[l, r]表示每个结点的区间"""
        if l > r: return  # 针对nums为空的情况
        if l == r:  # 来到叶子结点
            node = Node(l, r)
            node.merge_val = self._data[l]  # 叶子结点的区间和即为原始数组相应位置上的值
            return node
        node = Node(l, r)
        m = (l + r) // 2
        node.left = self._build_tree(l, m)  # 构造左区间，[l, m]
        node.right = self._build_tree(m + 1, r)  # 构造右区间，[m+1, r]
        node.merge_val = self._merger(node.left.merge_val, node.right.merge_val)  # 根据用户传进来的merger合并统计值
        return node

    def _update(self, root, idx, val):
        if root.start == root.end:  # 来到叶子结点
            root.merge_val = val  # 更新叶子结点值
            return
        m = (root.start + root.end) // 2
        if idx <= m:  # 要更新的索引小于等于区间中点，则去左区间更新
            self._update(root.left, idx, val)
        else:  # 否则去右区间更新
            self._update(root.right, idx, val)
        root.merge_val = self._merger(root.left.merge_val, root.right.merge_val)  # 返回时记得更新区间统计值

    def _query(self, root, l, r):
        if root.start == l and root.end == r:  # 左右边界恰好等于要查找的边界
            return root.merge_val
        m = (root.start + root.end) // 2
        if r <= m:  # 查找的右边界小于等于区间的中点，则去左区间查找
            return self._query(root.left, l, r)
        elif l > m:  # 查找的左边界大于区间中点，则去右区间查找
            return self._query(root.right, l, r)
        else:  # 否则把查找范围分割成两部分，分别在左右区间查找
            return self._merger(self._query(root.left, l, m), self._query(root.right, m + 1, r))

    def _level_order(self):
        if self._root is None: return []
        queue, res = [self._root], []
        while queue:
            node = queue.pop(0)
            res.append(node.merge_val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
