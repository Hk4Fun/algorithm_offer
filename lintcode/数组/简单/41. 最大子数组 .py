__author__ = 'Hk4Fun'
__date__ = '2018/3/28 17:52'
'''题目描述：
给定一个整数数组，找到一个具有最大和的子数组，返回其最大和。

注意事项：
子数组最少包含一个数

样例：
给出数组[−2,2,−3,4,−1,2,1,−5,3]，符合要求的子数组为[4,−1,2,1]，其最大和为6
'''
'''主要思路：
时间O（n），空间O（1）
动态规划，见target_offer31_连续子数组的最大和
'''


class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(curSum + num, num)
            maxSum = max(curSum, maxSum)
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