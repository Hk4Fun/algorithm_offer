__author__ = 'Hk4Fun'
__date__ = '2018/3/24 23:00'
'''题目描述：
给定一个排序的整数数组（升序）和一个要查找的整数target，
用O(logn)的时间查找到target第一次出现的下标（从0开始），
如果target不存在于数组中，返回-1。
注意：数组中有重复数字时返回第一个
样例：
在数组 [1, 2, 3, 3, 4, 5, 10] 中二分查找3，返回2。
'''


class Solution:
    def binarySearch(self, nums, target):
        """
        @param nums: The integer array.
        @param target: Target to find.
        @return: The first position of target. Position starts from 0.
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                # 对重复数字进行筛选
                if mid == 0 or nums[mid - 1] < nums[mid]:
                    return mid
                else:
                    right = mid - 1
        return -1


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

        testArgs.append([[1, 2, 3, 3, 4, 5, 10], 3, 2])
        testArgs.append([[1, 2, 3, 3, 4, 5, 10], 16, -1])
        testArgs.append([[1, 2, 3, 3, 4, 5, 10], 1, 0])
        testArgs.append([[1, 2, 3, 3, 4, 5, 10], 10, 6])
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
