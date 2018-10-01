__author__ = 'Hk4Fun'
__date__ = '2018/10/1 17:01'

from exceptions import EmptyError


class SegmentTree:
    def __init__(self, arr, merger):
        if not arr: raise EmptyError('arr should not empty')
        self._data = list(arr)
        self._merger = merger
        self._tree = [None] * (len(arr) * 4)
        self._build_tree(0, 0, self.size - 1)

    def __repr__(self):
        return 'SegmentTree([{}])'.format(','.join(repr(val) for val in self._tree))

    def __setitem__(self, idx, val):
        if not 0 <= idx < self.size:
            raise IndexError('invalid index')
        self._data[idx] = val  # 更新原始数据
        self._set(0, 0, self.size - 1, idx, val)  # 更新线段树

    @property
    def size(self):
        """返回原始数组的元素个数"""
        return len(self._data)

    def query(self, queryL, queryR):
        """返回区间[queryL, queryR]的统计值"""
        if not 0 <= queryL <= queryR < self.size:
            raise IndexError('invalid query index')
        return self._query(0, 0, self.size - 1, queryL, queryR)

    def _set(self, tree_idx, l, r, idx, val):
        """在以tree_idx为根([l...r]范围里)的线段树中更新idx的值为val"""
        if l == r:
            self._tree[tree_idx] = val
            return

        left_tree_idx = self._left_child(tree_idx)
        right_tree_idx = self._right_child(tree_idx)

        m = (l + r) // 2
        if idx <= m:
            self._set(left_tree_idx, l, m, idx, val)
        else:
            self._set(right_tree_idx, m + 1, r, idx, val)

        # 最后记得更新统计信息
        self._tree[tree_idx] = self._merger(self._tree[left_tree_idx], self._tree[right_tree_idx])

    def _query(self, idx, l, r, queryL, queryR):
        """在以idx为根([l...r]范围里)的线段树中，搜索区间[queryL...queryR]的值"""
        if l == queryL and r == queryR:
            return self._tree[idx]

        left_idx = self._left_child(idx)
        right_idx = self._right_child(idx)

        m = (l + r) // 2
        if queryR <= m:  # 查询范围全部落在左区域
            return self._query(left_idx, l, m, queryL, queryR)
        elif queryL > m:  # 查询范围全部落在右区域
            return self._query(right_idx, m + 1, r, queryL, queryR)

        # 查询范围同时落在左右区域，拆开查询
        left_res = self._query(left_idx, l, m, queryL, m)
        right_res = self._query(right_idx, m + 1, r, m + 1, queryR)
        return self._merger(left_res, right_res)  # 拆开查询时返回去需要合并

    def _build_tree(self, idx, l, r):
        """在idx的位置创建表示区间[l...r]的线段树"""
        if l == r:
            self._tree[idx] = self._data[l]
            return
        left_idx = self._left_child(idx)
        right_idx = self._right_child(idx)

        m = (l + r) // 2
        self._build_tree(left_idx, l, m)  # 左区域：[l, m]
        self._build_tree(right_idx, m + 1, r)  # 右区域：[m+1, r]

        self._tree[idx] = self._merger(self._tree[left_idx], self._tree[right_idx])

    def _left_child(self, idx):
        """返回下标为idx的结点的左孩子结点的下标"""
        return idx * 2 + 1

    def _right_child(self, idx):
        """返回下标为idx的结点的右孩子结点的下标"""
        return idx * 2 + 2
