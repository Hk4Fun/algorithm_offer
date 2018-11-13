__author__ = 'Hk4Fun'
__date__ = '2018/4/4 0:59'
'''题目描述：
Find the contiguous subarray within an array (containing at least one number) which has the largest product.
For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''
'''主要思路：
时间O（n），空间O（1）
乘积就要注意了：
小的值在后面可能会变成大的值，如一个负数乘另一个负数；
而大的值在后面可能会变成小的值，如一个正数乘另一个负数。
所以需要同时记录最小值和最大值
'''


class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxPro = small = big = nums[0]
        for num in nums[1:]:
            # 为了节省一个临时变量，这两个必须在一行
            small, big = min(num, small * num, big * num), max(num, small * num, big * num)
            maxPro = max(maxPro, big)
        return maxPro


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
    solution = Solution()
    MyTest(solution=solution).start_test()
