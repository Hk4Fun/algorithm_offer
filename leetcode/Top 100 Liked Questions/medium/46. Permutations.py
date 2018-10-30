__author__ = 'Hk4Fun'
__date__ = '2018/7/29 10:46'
'''题目描述：
Given a collection of distinct integers, 
return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
'''主要思路：
target_offer/28_1_字符串的排列.py 思路2
'''


class Solution:
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    def permute(self, nums):
        if len(nums) == 1: return [nums]
        res = []
        for i in range(len(nums)):
            for j in self.permute(nums[:i] + nums[i + 1:]):
                res.append(j + [nums[i]])
        return res

    def permute_simplify(self, nums):
        return [[n] + p
                for i, n in enumerate(nums)
                for p in self.permute_simplify(nums[:i] + nums[i + 1:])] or [[]]


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

        testArgs.append([[1, 2, 3], [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()
