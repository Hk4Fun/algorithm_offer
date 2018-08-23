__author__ = 'Hk4Fun'
__date__ = '2018/8/23 23:18'
'''题目描述：
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''
'''主要思路：
思路1（时间O（nlogn），空间O（1 or n））
先排序（如果过要求不能原地修改数组就要额外O（n）的空间，否则原地排序即可），然后线性扫描

思路2（时间O（n），空间O（n））
借助 union find 的思想，借助一个字典（hash table）实现

思路3（时间O（n），空间O（n））
利用集合，线性扫描，最简洁的思路
'''


class Solution:
    """
    :type nums: List[int]
    :rtype: int
    """

    def longestConsecutive1(self, nums):
        if not nums: return 0
        nums.sort()
        maxcount = curcount = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    curcount += 1
                else:
                    maxcount = max(maxcount, curcount)
                    curcount = 1
        return max(maxcount, curcount)

    def longestConsecutive2(self, nums):
        if not nums: return 0
        dic = {}  # 键：值 = nums中的数：该数所在连通区域的大小
        for n in nums:
            if n not in dic:
                l, r = dic.get(n - 1, 0), dic.get(n + 1, 0)  # 不存在就为0，保证下一行代码的正确性
                s = l + r + 1  # 连通左右区域，得到新的连通区域大小
                # 更新左右边界的连通区域大小，因为其他数在加入时总是获取边界上的数对应的连通区域大小
                dic[n] = dic[n - l] = dic[n + r] = s
        return max(dic.values())

    def longestConsecutive(self, nums):
        nums = set(nums)
        maxcount = 0
        for n in nums:
            if n - 1 not in nums:  # 先找到左边界，这样每个元素最多被扫描两次
                m = n + 1
                while m in nums:
                    m += 1
                maxcount = max(maxcount, m - n)
        return maxcount


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

        testArgs.append([[1, 2, 0, 1], 3])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()
