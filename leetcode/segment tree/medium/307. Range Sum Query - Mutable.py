__author__ = 'Hk4Fun'
__date__ = '2018/8/28 1:58'
'''题目描述：

'''
'''主要思路：
思路1：根据leetcode/dp/easy/303. Range Sum Query - Immutable.py的思路2
只需在更新操作中同时更新自己维护的dp数组就可以了，但这样更新操作的时间为O(n)，直接TLE了

思路2：动态更新并获取某段区间的统计信息（这里是求和），线段树再适合不过
'''


class Node:
    '''线段树上的每个结点'''

    def __init__(self, start, end):
        self.start = start  # 区间左边界
        self.end = end  # 区间右边界
        self.total = 0  # 区间和
        self.left = self.right = None  # 左右孩子结点


class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        def build_tree(l, r):
            """递归构造线段树，[l, r]表示每个结点的区间"""
            if l > r: return  # 针对nums为空的情况
            if l == r:  # 来到叶子结点
                node = Node(l, r)
                node.total = nums[l]  # 叶子结点的区间和即为原始数组相应位置上的值
                return node
            node = Node(l, r)
            m = (l + r) // 2
            node.left = build_tree(l, m)  # 构造左区间，[l, m]
            node.right = build_tree(m + 1, r)  # 构造右区间，[m+1, r]
            node.total = node.left.total + node.right.total  # 当前区间和为左右区间和的和
            return node

        self.root = build_tree(0, len(nums) - 1)  # 根结点的区间为[0, len(nums)-1]

    def update(self, idx, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """

        def setitem(root, idx, val):
            if root.start == root.end:  # 来到叶子结点
                root.total = val  # 更新叶子结点值
                return
            m = (root.start + root.end) // 2
            if idx <= m:  # 要更新的索引小于等于区间中点，则去左区间更新
                setitem(root.left, idx, val)
            else:  # 否则去右区间更新
                setitem(root.right, idx, val)
            root.total = root.left.total + root.right.total  # 返回时记得更新区间和

        setitem(self.root, idx, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """

        def rangeSum(root, i, j):
            if root.start == i and root.end == j:  # 左右边界恰好等于要查找的边界
                return root.total
            m = (root.start + root.end) // 2
            if j <= m:  # 查找的右边界小于等于区间的中点，则去左区间查找
                return rangeSum(root.left, i, j)
            elif i > m:  # 查找的左边界大于区间中点，则去右区间查找
                return rangeSum(root.right, i, j)
            else:  # 否则把查找范围分割成两部分，分别在左右区间查找
                return rangeSum(root.left, i, m) + rangeSum(root.right, m + 1, j)

        return rangeSum(self.root, i, j)


if __name__ == '__main__':
    arr = NumArray([1, 2, 3])
    arr.update(0, -1)
    print(arr.sumRange(0, 1))
