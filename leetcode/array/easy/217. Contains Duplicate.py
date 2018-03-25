__author__ = 'Hk4Fun'
__date__ = '2018/3/25 19:18'
'''题目描述：
Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
'''
'''主要思路：
思路1（时间O（nlogn），空间O（1））：排序
思路2（时间O（n），空间O（n））：哈希
思路3：pythonic，集合去重
'''


class Solution(object):
    def containsDuplicate_sort(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

    def containsDuplicate_dict(self, nums):
        d = {}
        for num in nums:
            if num in d:
                return True
            d[num] = None
        return False

    def containsDuplicate_set(self, nums):
        return len(set(nums)) != len(nums)


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

        testArgs.append([[1, 2, 3], False])
        testArgs.append([[1, 2, 3, 3], True])

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
