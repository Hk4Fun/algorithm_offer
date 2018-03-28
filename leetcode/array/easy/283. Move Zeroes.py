__author__ = 'Hk4Fun'
__date__ = '2018/3/28 15:53'
'''题目描述：
Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.
For example, given nums = [0, 1, 0, 3, 12], 
after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
'''主要思路：
思路1：时间O（n），空间O（1）
双指针，快指针j遇到不是0的数就往i上放，然后ij都移动，
j来到末尾停止，此时让i往后填充0即可
思路2：时间O（n），空间O（1）
上个思路是覆盖，然后填充，那么可以这样想：
把覆盖换成交换，这样填充步骤就可省略了：
j遇到非0数时与i交换，然后ij都移动，否则j一直往前移动，直到来到末尾，
这样i之前的数都是非0数，而i与j之间的数都是0
这样可以优化数组的访问次数：比如[0,0,0,0,1]
思路1要覆盖1次，填充4次；而思路2只需交换1次

注意到：每次交换i要么等于j，要么i上的数就是0，这样才能保证j一直往前，
不可能在i不等与j时，对于j来讲交换过来的数是非0数。
当然，在最坏的情况下，数组中的每个数都是非0数时，两个思路的访问次数差不多
但可能思路2会更慢，毕竟交换是比覆盖要慢的
'''


class Solution:
    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:  # 收集不是0的数
                nums[i] = nums[j]
                i += 1
        for k in range(i, len(nums)):  # 填充被覆盖掉的0
            nums[k] = 0
        return nums  # for test

    def moveZeroes2(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]  # 改成交换而不是覆盖
                i += 1
        return nums  # for test


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 10000  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([[0, 1, 0, 3, 12], [1, 3, 12, 0, 0]])
        testArgs.append([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]])
        testArgs.append([[0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0]])

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
