__author__ = 'Hk4Fun'
__date__ = '2018/7/29 7:17'
'''题目描述：
Given an array nums of n integers where n > 1,  
return an array output such that output[i] is equal to 
the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''
'''主要思路：
target_offer/52_构建乘积数组.py
时间O（n），空间O（1）:
B[i]=C[i]*D[i]=(A[0]*A[1]*...*A[i-1])*(A[i+1]*...*A[n-1])
C[i]=C[i-1]*A[i-1], D[i]=A[i+1]*D[i+1]
利用数组B的空间来节省数组C和D的空间
关键之处，D[i]只与D[i+1]有关，因此可以节约空间为O(1)
'''


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        res = [1] * len(nums)
        for i in range(1, len(nums)):  # 求出所有C[i]
            res[i] = nums[i - 1] * res[i - 1]
        tmp = 1  # 关键之处，D[i]只与D[i+1]有关，因此可以节约空间为O(1)
        for i in range(len(nums) - 2, -1, -1):
            tmp *= nums[i + 1]  # D[i]
            res[i] *= tmp  # C[i]*D[i]
        return res


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
