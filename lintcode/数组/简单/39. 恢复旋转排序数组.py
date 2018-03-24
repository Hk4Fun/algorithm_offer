__author__ = 'Hk4Fun'
__date__ = '2018/3/24 23:33'
'''题目描述：
给定一个旋转排序数组，在原地恢复其排序。
样例:
[4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]
'''
'''主要思路：
时间O（n），空间O（1）
target_offer中第8题和第42_2的综合：
找到旋转数组的最小数字下标n，然后循环左移n即可恢复
'''


class Solution:
    def recoverRotatedSortedArray(self, nums):
        """
        @param nums: An integer array
        @return: nothing
        """

        def find(nums):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + ((right - left) >> 1)
                if nums[mid] > nums[right]:
                    left = mid + 1
                elif nums[mid] < nums[right]:
                    if mid == 0 or nums[mid - 1] > nums[mid]:
                        return mid
                    else:
                        right = mid - 1
                else:
                    right = right - 1
            return left

        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        def rotate(nums, n):
            reverse(nums, 0, n - 1)
            reverse(nums, n, len(nums) - 1)
            reverse(nums, 0, len(nums) - 1)

        rotate(nums, find(nums))
        return nums  # 为了测试方便返回nums


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

        testArgs.append([[4, 5, 1, 2, 3], [1, 2, 3, 4, 5]])
        testArgs.append([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
        testArgs.append([[1, 0, 1, 1, 1], [0, 1, 1, 1, 1]])
        testArgs.append([[1, 1, 1, 0, 1], [0, 1, 1, 1, 1]])
        testArgs.append([[2], [2]])
        testArgs.append([[3, 4, 5, 5, 1, 2], [1, 2, 3, 4, 5, 5]])
        testArgs.append([[3, 4, 5, 1, 1, 2], [1, 1, 2, 3, 4, 5]])
        testArgs.append([[3, 4, 5, 1, 2, 2], [1, 2, 2, 3, 4, 5]])

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
