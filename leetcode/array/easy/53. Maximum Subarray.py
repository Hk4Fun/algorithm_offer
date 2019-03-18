__author__ = 'Hk4Fun'
__date__ = '2018/3/24 21:50'
'''题目描述：
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''
'''主要思路：
target_offer/31_连续子数组的最大和.py
动态规划：
设f(i)为以第i个数结尾的连续子数组的最大和，则状态转移方程为：
f(i) = max(f(i-1)+array[i], array[i])
最后结果为max(f(i))
优化：f(i)只与f(i-1)有关，即只与前一状态有关，所以空间上可以由O(n)降为O(1)
'''


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum, maxSum = 0, -float('inf')
        for num in nums:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
        return maxSum


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([[1, -2, 3, 10, -4, 7, 2, -5], 18])

        # 所有数字都是负数
        testArgs.append([[-2, -8, -1, -5, -9], -1])

        # 所有数字都是正数
        testArgs.append([[2, 8, 1, 5, 9], 25])

        # 只有一个数字
        testArgs.append([[0], 0])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
