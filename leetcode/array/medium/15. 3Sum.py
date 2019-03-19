__author__ = 'Hk4Fun'
__date__ = '2018/4/8 16:38'
'''题目描述：
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''
'''主要思路：
时间O（n^2），空间O（1）
先排序，然后遍历每个数作为和的第一个数，这样就把问题转化为 
167.Two Sum II - Input array is sorted（双指针）
需要注意的地方：避免出现重复的答案，这里有两个地方需要跳过：
1、双指针的活动范围是作为第一个数的右边的数，左边不必再考虑，
因为左边如果存在这样的数，那么在第一个数遍历到它的时候应该就已经添加过了
这三个数实际上是没有先后之分的，我们只是固定了一个数，使问题为2sum罢了
2、三个指针在移动时如果遇到相同的数应该跳过
'''


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 2):  # 每次固定一个数
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i - 1]: continue  # 跳过重复值
            l, r = i + 1, len(nums) - 1  # 只考虑右边的数，左边已经检查过
            while l < r:
                s = nums[l] + nums[r] + nums[i]
                if s < 0:  # 如果遇到重复值，那么下一循环自然还会命中这一行
                    l += 1
                elif s > 0:
                    r -= 1
                else:  # 找到后接着找，而不是break
                    res += [nums[i], nums[l], nums[r]],
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: l += 1  # 跳过重复值，否则会重复添加
                    # r不用-1，因为下一循环一定是nums[l] + nums[r] + nums[i] > 0， 即 s > 0, r -= 1
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

        testArgs.append([[-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]])
        testArgs.append([[0, 0, 0, 0], [[0, 0, 0]]])
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
