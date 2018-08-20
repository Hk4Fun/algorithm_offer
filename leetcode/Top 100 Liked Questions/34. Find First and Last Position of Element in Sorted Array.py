__author__ = 'Hk4Fun'
__date__ = '2018/8/20 17:25'
'''题目描述：
Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''
'''主要思路：
思路1：
target_offer/38_1_数字在排序数组中出现的次数.py
时间O（logn），空间O（1）

思路2：
使用标准库bisect:
bisect.bisect_left(nums, target)：获取target在nums中第一次出现的位置
bisect.bisect(nums, target) - 1 ：获取target在nums中最后一次出现的位置
'''

import bisect


class Solution:
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    def searchRange1(self, nums, target):
        def findfirst():
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] > target:
                    hi = mid - 1
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    if mid == 0 or nums[mid - 1] < target:
                        return mid
                    else:
                        hi = mid - 1
            return -1

        def findlast():
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] > target:
                    hi = mid - 1
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    if mid == len(nums) - 1 or nums[mid + 1] > target:
                        return mid
                    else:
                        lo = mid + 1
            return -1

        return [findfirst(), findlast()]

    def searchRange2(self, nums, target):
        # 注意这里的切片可以避免触发异常：切片不存在时返回空的list
        lo = bisect.bisect_left(nums, target)
        return [lo, bisect.bisect(nums, target) - 1] if target in nums[lo:lo + 1] else [-1, -1]


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
