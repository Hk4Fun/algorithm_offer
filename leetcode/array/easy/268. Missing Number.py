__author__ = 'Hk4Fun'
__date__ = '2018/3/28 15:07'
'''题目描述：
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

Example 1
Input: [3,0,1]
Output: 2

Example 2
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
'''
'''主要思路：
target_offer38_2缺失的数字，注意这里是未排序的，
所以除了求和公式和排序二分以外，这里介绍另一种思路：
位运算：时间O（n），空间O（1）
这里有0~n共n+1个数字，而下标为0~n-1，
所以可以补上一个n然后把所有下标和对应的数字异或起来，
这样缺失的那个数字就是异或结果
（不必担心是否排序，反正最后会被异或消掉，
而缺失的那个数字对应的下标没被消掉）
'''


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missing = len(nums)
        for i, v in enumerate(nums):
            missing ^= i ^ v
        return missing


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

        testArgs.append([[1, 2, 3, 4, 5], 0])  # 缺失的是第一个数字0
        testArgs.append([[0, 1, 2, 3, 4], 5])  # 缺失的是最后一个数字
        testArgs.append([[0, 1, 2, 4, 5], 3])  # 缺失的是中间某个数字0
        testArgs.append([[1], 0])  # 数组中只有一个数字，缺失的是第一个数字0
        testArgs.append([[0], 1])  # 数组中只有一个数字，缺失的是最后一个数字1

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
