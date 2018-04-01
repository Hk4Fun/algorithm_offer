__author__ = 'Hk4Fun'
__date__ = '2018/4/1 11:30'
'''题目描述：
Given a non-empty array of non-negative integers nums, 
the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, 
that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6

Note:
nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
'''
'''主要思路：
时间O（N），空间O（N）
第一遍扫描数组，记录每个数出现的次数count、最左边的位置first和最右边的位置last；
则degree = max(count.values())
第二遍扫描count，找出出现次数为degree的最小长度：minLen = min(minLen, last[num] - first[num] + 1)
'''

from collections import Counter


class Solution:
    """
    :type nums: List[int]
    :rtype: int
    """

    def findShortestSubArray1(self, nums):
        count, first, last = {}, {}, {}
        for i, v in enumerate(nums):
            if v not in first:
                first[v] = i
            last[v] = i
            count[v] = count.get(v, 0) + 1
        minLen = float('inf')
        degree = max(count.values())
        for num in count:
            if count[num] == degree:
                minLen = min(minLen, last[num] - first[num] + 1)
        return minLen

    def findShortestSubArray2(self, nums):  # 简化版
        count, first, last = Counter(nums), {}, {}
        for i, v in enumerate(nums):
            first.setdefault(v, i)
            last[v] = i
        degree = max(count.values())
        return min(last[num] - first[num] + 1 for num in count if count[num] == degree)


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

        testArgs.append([[1, 2, 2, 3, 1], 2])
        testArgs.append([[1, 2, 2, 3, 1, 4, 2], 6])

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
