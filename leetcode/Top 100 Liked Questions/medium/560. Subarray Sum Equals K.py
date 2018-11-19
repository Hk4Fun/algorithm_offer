__author__ = 'Hk4Fun'
__date__ = '2018/8/11 21:33'
'''题目描述：
Given an array of integers and an integer k, 
you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''
'''主要思路：
思路1：时间O（n^2），空间O（1）--TLE
对于每个起始点，一边累加一遍检查是否达到k，当sum为k时count++，然后继续往下遍历即可（数组可能存在负数）

思路2：时间O（n），空间O（n）
hash表存储从下标0到每个下标的和所出现的次数，则对于下标i和j，若sum(j)-sum(i)=k，即sum(j)-k=sum(i)
则说明从i到j之间的数的和为k，count加上前面sum(i)出现的次数
也就是说如果sum(j)-k=sum(i)在hash表中出现过，说明存在和为k的子数组，就是在i和j之间
而和为k的子数组出现的次数就是之前sum(i)出现的次数
'''


class Solution:
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    def subarraySum1(self, nums, k):
        length = len(nums)
        count = 0
        for start in range(length):
            sum = 0
            for end in range(start, length):
                sum += nums[end]
                if sum == k:
                    count += 1
        return count

    def subarraySum2(self, nums, k):
        count = sum = 0
        hashmap = {0: 1}  # 考虑到第一个数就等于k，则sum-k=0，应该命中
        for num in nums:
            sum += num  # 累计当前和
            count += hashmap.get(sum - k, 0)  # count加上前面sum(i)=sum-k出现的次数
            hashmap[sum] = hashmap.setdefault(sum, 0) + 1  # 存储从下标0到每个下标的和所出现的次数
        return count


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
