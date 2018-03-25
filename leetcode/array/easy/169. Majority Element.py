__author__ = 'Hk4Fun'
__date__ = '2018/3/25 18:14'
'''题目描述：
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊n/2⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
'''
'''主要思路：
思路1（时间O（n），空间O（1））：
target_offer的29_数组中出现次数超过一半的数字的思路2

思路2（时间（最坏：正无穷，最好：O（1）），空间O（1））：
从数组中随机选一个数，检查是否超过一半，否则继续
该算法为多数投票算法(Boyer-Moore Algorithm)

在n很大时时思路2其实比思路1要快，当然前提是保证数组中的确存在超过一半的数字
'''

import random


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        master = nums[0]  # 先让第一个数作为守阵地的士兵，
        HP = 1  # 初始都为一滴HP
        for i in range(1, len(nums)):
            if HP == 0:  # 当HP削减为0时，以下一个数作为守阵地的士兵
                master = nums[i]
                HP = 1
            elif nums[i] == master:  # 遇到相同元素，相当于支援兵，补血，HP+1
                HP += 1
            else:  # 遇到不相同元素，相当于敌人，掉血，HP-1
                HP -= 1
        return master

    def majorityElement_simple(self, nums):
        # 上一思路的简化版
        count, candidate = 0, None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)  # 合并了

        return candidate

    def majorityElement_random(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while True:
            r = random.choice(nums)
            if nums.count(r) >= len(nums) // 2:
                return r


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

        # 存在出现次数超过数组长度一半的数字
        testArgs.append([[1, 2, 3, 2, 2, 2, 5, 4, 2], 2])

        # 出现次数超过数组长度一半的数字都出现在数组的前半部分
        testArgs.append([[2, 2, 2, 2, 2, 1, 3, 4, 5], 2])

        # 出现次数超过数组长度一半的数字都出现在数组的后半部分
        testArgs.append([[1, 3, 4, 5, 2, 2, 2, 2, 2], 2])

        # 只有一个数
        testArgs.append([[1], 1])

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
