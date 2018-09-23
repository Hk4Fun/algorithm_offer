__author__ = 'Hk4Fun'
__date__ = '2018/8/28 1:58'
'''题目描述：

'''
'''主要思路：
思路1：根据leetcode/dp/easy/303. Range Sum Query - Immutable.py的思路2
只需在更新操作中同时更新自己维护的dp数组就可以了，但这样更新操作的时间为O(n)，直接TLE了

思路2：动态更新并获取某段区间的统计信息（这里是求和），线段树再适合不过

思路3：既然能用线段树来解决，那就可以考虑树状数组

思路4：RMQ?
'''


class NumArray1:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums[:]
        self.sum = [0]
        for n in nums:
            self.sum += (self.sum[-1] + n),

    def update(self, idx, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.nums[idx] = val
        for i in range(idx + 1, len(self.nums) + 1):  # 这里记得+1，因为self.nums向右偏了1位
            self.sum[i] = self.sum[i - 1] + self.nums[i - 1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum[j + 1] - self.sum[i]
