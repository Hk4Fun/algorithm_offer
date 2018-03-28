__author__ = 'Hk4Fun'
__date__ = '2018/3/28 16:52'
'''题目描述：
Given a non-empty array of integers, return the third maximum number in this array. 
If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]
Output: 1
Explanation: The third maximum is 1.

Example 2:
Input: [1, 2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: [2, 2, 3, 1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''
'''主要思路：
思路1（时间O（n），空间O（1））:
求第k大的数，只不过这里k是固定的（k=3），所以可以用长度为3的数组存放最大的三个数并依次比较
思路2（时间O（n），空间O（1））：
一般化解法，使用优先队列（最小堆）
思路3（时间O（?），空间O（1））：
使用partition，但前提是用set()来去重，这一步是相当耗时的，
在leetcode上是 'Time Limit Exceeded' 的
'''

from heapq import *


class Solution:
    def thirdMax1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = [-float('inf')] * 3
        for num in nums:
            if num not in l:
                if num > l[0]:
                    l = [num, l[0], l[1]]
                elif num > l[1]:
                    l = [l[0], num, l[1]]
                elif num > l[2]:
                    l = [l[0], l[1], num]
        return max(nums) if -float('inf') in l else l[2]

    def thirdMax2(self, nums):
        pq = []
        for num in nums:
            if len(pq) < 3 and num not in pq:
                heappush(pq, num)
            elif num > pq[0] and num not in pq:
                heappushpop(pq, num)
        if len(pq) < 3:  # 小于三个返回最大值
            while len(pq) != 1:
                heappop(pq)
        return pq[0]

    def thirdMax3(self, nums):
        def partition(nums, l, r):
            i, j = l, r
            pivot = nums[l]
            while i < j:
                while i < j and nums[j] > pivot: j -= 1
                if i < j:
                    nums[i] = nums[j]
                    i += 1
                while i < j and nums[i] < pivot: i += 1
                if i < j:
                    nums[j] = nums[i]
                    j -= 1
            nums[i] = pivot
            return i

        nums = list(set(nums))
        l, r = 0, len(nums) - 1
        if len(nums) < 3: return max(nums)
        k = len(nums) - 3
        while l <= r:
            index = partition(nums, l, r)
            if index < k:
                l = index + 1
            elif index > k:
                r = index - 1
            else:
                return nums[index]


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

        testArgs.append([[3, 2, 1], 1])
        testArgs.append([[4, 3, 2, 1], 2])
        testArgs.append([[1, 1, 2, 2], 2])
        testArgs.append([[2, 2, 3, 1], 1])
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
