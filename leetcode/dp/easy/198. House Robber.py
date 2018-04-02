__author__ = 'Hk4Fun'
__date__ = '2018/4/2 17:17'
'''题目描述：
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that 
adjacent houses have security system connected and 
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.
'''
'''主要思路：
时间O（n），空间O（1）
dp[i]表示从开始抢到第i家店时所获取的最多金钱数量，则dp[i] = max(dp[i-1], dp[i-2] + nums[i])
表示要么抢当前这家店i，要么不抢
抢的话，那么所获取金钱最多可达 dp[i-2] + nums[i]，即前一家店不能抢，从开始抢到上上一家店的钱加上当前这家店的钱；
不抢的话，那么上一家店能抢，于是等于从开始抢到上一家店的钱
'''


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0 # 没有店可抢
        if len(nums) == 1: return nums[0] # 只有一家店可抢
        prepre = nums[0]
        pre = max(nums[0], nums[1])
        for x in nums[2:]:
            cur = max(prepre + x, pre)
            prepre = pre
            pre = cur
        return pre # 返回pre而不是cur是考虑到如果只有两家店，那么cur是不存在的


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
