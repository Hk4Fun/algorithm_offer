__author__ = 'Hk4Fun'
__date__ = '2018/3/24 18:15'
'''题目描述：
Given an array of integers, return indices of the two nums such that 
they add up to a specific target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
'''主要思路：
思路1：时间O（n），空间0（n）
用字典建立哈希表：
从左至右扫描数组，对于每个数字n，字典键为target-n，值为对应的数组下标，
如果n在字典中已经存在，说明之前出现过该数的配对数n'，否则target-n'不会等于它，下标直接获得

思路2：时间O（nlogn），空间0（n）
复制原数组并排序然后首尾双指针，找到后在原数组中找到该数字的下标（前提：数组无重复数字）
'''


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, v in enumerate(nums):
            if target - v in dic:
                return [dic[target - v], i]
            else:
                dic[v] = i


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

        testArgs.append([[2, 7, 11, 15], 9, [0, 1]])
        testArgs.append([[2, 7, 11, 15], 18, [1, 2]])
        testArgs.append([[2, 7, 11, 15], 7, None])
        testArgs.append([[2, 7, 11, 15], 1, None])
        testArgs.append([[2, 7, 11, 15], 16, None])
        testArgs.append([[2], 2, None])

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
