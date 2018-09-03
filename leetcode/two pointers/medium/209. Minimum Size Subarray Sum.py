__author__ = 'Hk4Fun'
__date__ = '2018/9/3 8:45'
'''题目描述：
Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s. 
If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, 
try coding another solution of which the time complexity is O(n log n). 
'''
'''主要思路：
时间O（n），空间O（1）
滑动窗口
'''


class Solution:
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """

    def minSubArrayLen1(self, s, nums):
        if not nums: return 0
        i = j = 0
        min_len = len(nums) + 1  # min_len初始值取一个max_int
        length = 1
        total = nums[0]
        while j < len(nums):
            if total <= s:
                if total == s:
                    min_len = min(length, min_len)
                j += 1
                length += 1
                if j < len(nums):
                    total += nums[j]
            else:
                min_len = min(length, min_len)
                total -= nums[i]
                i += 1
                length -= 1
        return min_len if min_len != len(nums) + 1 else 0

    def minSubArrayLen2(self, s, nums):  # 简化一下
        l, r = 0, -1  # nums[l...r]为滑动窗口，初始窗口没有包含任何数
        total = 0
        min_len = len(nums) + 1
        while l < len(nums):  # r到了右边界不动时，l还可以往右边界移动
            if total < s and r + 1 < len(nums):
                r += 1
                total += nums[r]
            else:
                total -= nums[l]
                l += 1
            if total >= s:
                min_len = min(min_len, r - l + 1)
        return min_len if min_len != len(nums) + 1 else 0

    def minSubArrayLen3(self, s, nums):  # 另一种实现
        total = left = 0
        min_len = len(nums) + 1
        for right, n in enumerate(nums):
            total += n
            while total >= s:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1
        return min_len if min_len != len(nums) + 1 else 0


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1000  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([11, [12, 1, 2, 3, 4, 5], 1])
        testArgs.append([11, [1, 2, 3, 4, 5], 3])
        testArgs.append([3, [1, 1], 0])
        testArgs.append([15, [1, 2, 3, 4, 5], 5])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()
