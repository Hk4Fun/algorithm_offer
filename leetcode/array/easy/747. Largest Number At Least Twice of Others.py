__author__ = 'Hk4Fun'
__date__ = '2018/4/1 18:19'
'''题目描述：
In a given integer array nums, there is always exactly one largest element.
Find whether the largest element in the array is at least twice as much as every other number in the array.
If it is, return the index of the largest element, otherwise return -1.

Example 1:
Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
 
Example 2:
Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.

Note:
nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].
'''
'''主要思路：
时间O（n），空间O（1）
找出最大值后，不用再遍历数组检测每个数是否满足，只要检测第二大的数是否满足即可，
它满足了其他比它小的数肯定也是满足的
'''


class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1: return 0  # 一定要有这个，否则只有一个数时，后面del就不能找第二大的数
        max1 = max(nums)  # 最大值
        idx = nums.index(max1)
        del nums[idx]  # 先删掉最大值
        max2 = max(nums)  # 第二大值
        return idx if max2 * 2 <= max1 else -1


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

        testArgs.append([[3, 6, 1, 0], 1])
        testArgs.append([[1, 2, 3, 4], -1])
        testArgs.append([[1], 0])

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
