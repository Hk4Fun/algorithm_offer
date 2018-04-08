__author__ = 'Hk4Fun'
__date__ = '2018/4/8 19:40'
'''题目描述：
Given an array S of n integers, are there elements a, b, c, 
and d in S such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.
Note: The solution set must not contain duplicate quadruplets.
For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
'''主要思路：
时间O（n^3），空间O（1）
套路是一样的，固定两个，转成2sum，所以可以发现nSum的规律了：
对于nSum，其时间复杂度复杂度为O(N^(n-1))，N表示数组的长度
这里直接写一个nSum的解法了：
外层套n-2层循环，最终转化成2sum，这里递归实现
'''


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def nSum(nums, start, target, N, result, results):  # 使用start是为了避免切片而增加空间消耗
            if len(nums[start:]) < N or N < 2: return
            if N == 2:  # 2Sum
                l, r = start, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]: l += 1  # 跳过重复值
            else:
                for i in range(len(nums[start:]) - N + 1):
                    if target < nums[i] * N or target > nums[-1] * N: break  # 提前结束（仔细想想为什么:)）
                    if i > 0 and nums[start + i] == nums[start + i - 1]: continue  # 跳过重复值
                    nSum(nums, start + i + 1, target - nums[start + i], N - 1, result + [nums[start + i]], results)

        results = []
        nums.sort()
        nSum(nums, 0, target, 4, [], results)
        return results


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
    solution = Solution()
    MyTest(solution=solution).start_test()
