__author__ = 'Hk4Fun'
__date__ = '2018/4/2 17:33'
'''题目描述：
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''
'''主要思路：
思路1（初始化时间O（1），求和时间O（n），空间O（1））
思路2（初始化时间O（n），求和时间O（1），空间O（n））
'''


class NumArray1:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j + 1])


class NumArray2:
    def __init__(self, nums):
        self.dp = nums[:]  # 不能改变原数组，所以只能缓存
        for i in range(1, len(nums)):
            self.dp[i] += self.dp[i - 1]

    def sumRange(self, i, j):
        return self.dp[j] - (self.dp[i - 1] if i > 0 else 0)


class NumArray3:  # NumArray2的改进
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.dp = [0]
        for num in nums:
            self.dp += self.dp[-1] + num,

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j + 1] - self.dp[i]
