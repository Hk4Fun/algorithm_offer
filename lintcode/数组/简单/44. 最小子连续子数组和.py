__author__ = 'Hk4Fun'
__date__ = '2018/3/25 0:25'
'''题目描述：

'''
'''主要思路：
时间O（n），空间O（1）
将最大连续子数组和中的max改成min即可
'''


class Solution:
    def minSubArray(self, nums):
        """
        @param: nums: a list of integers
        @return: A integer indicate the sum of minimum subarray
        """
        curSum = minSum = nums[0]
        for num in nums[1:]:
            curSum = min(num, curSum + num)
            minSum = min(minSum, curSum)
        return minSum


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

        testArgs.append([[1, -1, -2, 1], -3])

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
