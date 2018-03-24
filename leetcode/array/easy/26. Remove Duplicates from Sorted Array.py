__author__ = 'Hk4Fun'
__date__ = '2018/3/24 19:02'
'''题目描述：
Given a sorted array, remove the duplicates in-place such that 
each element appear only once and return the new length.
Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.

Example:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
'''
'''主要思路：
空间O（1），时间O（n）
双指针：
由于数组是有序数组，所以让j作为快指针在前面负责收集不同的数，
一旦nums[j] != nums[i], 则nums[++i] = nums[j]
然后j接着往后走继续收集，直到来到数组末尾，这样i前面（包括i）保存都是不重复的数字
'''


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        for j in range(len(nums)):
            if nums[i] != nums[j]: # 先移动再复制
                i += 1
                nums[i] = nums[j]
        return i + 1


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

        testArgs.append([[1, 1, 2, 3, 4], 4])
        testArgs.append([[1, 1, 2, 2, 3, 3], 3])
        testArgs.append([[1, 1, 2, 3, 3, 4, 4], 4])
        testArgs.append([[1, 2, 3, 4], 4])
        testArgs.append([[1, 1, 1, 1], 1])
        testArgs.append([[1], 1])
        testArgs.append([[], 0])

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
