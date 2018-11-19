__author__ = 'Hk4Fun'
__date__ = '2018/8/12 11:22'
'''题目描述：
Given a non-empty array containing only positive integers, 
find if the array can be partitioned into two subsets 
such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
'''
'''主要思路：
思路1：dp
leetcode/Top 100 Liked Questions/494. Target Sum.py 思路2
这里转换一下，相当于求集合中是否存在和为 sum(nums)/2 的子集（不一定有序）
Target Sum 中是求集合中和为某个数的子集个数，所以这里可以直接用 Target Sum 中的dp算法
只不过最后结果返回 dp[target]>0 而不是 dp[target]

思路2：暴力
枚举所有子集的和，一边求一边判断

思路3：sort然后dfs，不加lru_cache会TLE
'''

from functools import reduce, lru_cache


class Solution:
    """
    :type nums: List[int]
    :rtype: bool
    """

    def canPartition1(self, nums):
        s = sum(nums)
        if s & 1: return False  # 总和为奇数，这一定不存在
        target = sum(nums) // 2
        dp = [1] + [0] * target # 注意初始状态的设定
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] + dp[i - num] # 注意i的左边界为num，否则i-num越界
        return dp[target] > 0

    def canPartition2(self, nums):
        if sum(nums) & 1 == 0:
            target = sum(nums) >> 1
            cur = {0}
            for i in nums:
                cur |= {i + x for x in cur}  # 枚举所有子集的和
                if target in cur:  # 一边求一边判断
                    return True
        return False

    def canPartition3(self, nums):  # 上一思路的简化版，用reduce一行解决
        return (sum(nums) / 2.) in reduce(lambda cur, x: cur | {v + x for v in cur}, nums, {0})
        # 这里的 ‘/ 2.’ 兼容py2和py3

    def canPartition(self, nums):
        @lru_cache(1024)  # 不加缓存会TLE
        def dfs(start, target):
            if target < 0: return False
            if target == 0: return True
            for i, v in enumerate(nums[start:], start):
                if dfs(i + 1, target - v): return True
            return False

        nums.sort(reverse=True)
        return False if sum(nums) & 1 else dfs(0, sum(nums) // 2)


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = True  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()
