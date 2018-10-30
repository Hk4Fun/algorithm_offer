__author__ = 'Hk4Fun'
__date__ = '2018/3/28 18:50'
'''题目描述：
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), 
some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? 
You may assume the returned list does not count as extra space.

Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[5,6]
'''
'''主要思路：
时间O（n），空间O（1）
思路1：
把数组中的数当作下标（记得-1），然后把对应的数改成负数（如果已经是负数就不变）
再次遍历数组，不为负数的下标就是未被访问过的下标，也就是那些缺失的数（记得+1）

思路2：
借助 target_offer/51_数组中重复的数字.py 中的思路1
把所有数字放到与其下标相等的位置（这题数字都要-1，保证和下标对应），
遇到相等的说明发生了重复，跳过即可
这样最后再次遍历数组，那些下标与数字不对应的下标就是缺失的数字（下标+1）
'''


class Solution:
    def findDisappearedNumbers1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])  # 强行改为负数，为负数时不变
        return [i + 1 for i, v in enumerate(nums) if v > 0]  # 找到那些不为负数的下标

    def findDisappearedNumbers2(self, nums):
        i = 0
        while i < len(nums):
            idx = nums[i] - 1  # 数字要-1才能与下标对应
            if nums[i] != nums[idx]:  # 只交换数字不移动下标，因为换过来的数字还未检查
                nums[i], nums[idx] = nums[idx], nums[i]
            else:  # 下标对应或发生重复时只移动下标
                i += 1
        return [i + 1 for i, v in enumerate(nums) if i + 1 != v]  # 找到那些下标与数字不对应的下标


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

        testArgs.append([[4, 3, 2, 7, 8, 2, 3, 1], [5, 6]])
        testArgs.append([[1, 1, 1], [2, 3]])
        testArgs.append([[1, 2, 3, 4], []])

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
