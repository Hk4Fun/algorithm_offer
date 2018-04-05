__author__ = 'Hk4Fun'
__date__ = '2018/4/4 20:54'
'''题目描述：
Note: This is an extension of House Robber.
After robbing those houses on that street, 
the thief has found himself a new place for his thievery 
so that he will not get too much attention. 
This time, all houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. 
Meanwhile, the security system for these houses remain the same as for those in the previous street.
Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.
'''
'''主要思路：
时间O（n），空间O（1）
既然是House Robber的拓展，那么可以从House Robber中借鉴思路，或者把该问题转化成House Robber：
最关键的不同点在于之前抢某家店不用考虑后面还会出现一个循环回来的邻居，所以为了转换成House Robber，
我们可以考虑把这个环给‘断开’：
随便选一个断开点，设这个点左边那家店是i，右边那家店是i+1，分别考虑这两家店是否纳入抢的范围内：
1、不抢第i家店，也就是不把第i家店放在打算抢的范围内，这样就转换成了House Robber，
   使得即使其动态规划的结果中i+1和i-1被抢了也不会触发警报；
2、把第i家店考虑在打算抢的范围内，但是不抢第i+1家店，再次转换成了House Robber，
   这样即使i和i+2被抢了也不用担心触发警报
3、i和i+1都不抢，这种情况其实在情况1和情况2中已经包含了。

注意：考虑抢并不一定会抢，不考虑抢则一定不会抢，最终抢没抢，由动态规划的结果决定。
      考虑这两种情况只是为了保证动态规划的结果一定不会触发警报。
      (这里选择i=0,i+1=n-1,当然只要是相邻的两家店都可以得到一样的结果)
'''


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def rob(nums):  # House Robber
            if not nums: return 0  # 没有店可抢
            if len(nums) == 1: return nums[0]  # 只有一家店可抢
            prepre = nums[0]
            pre = max(nums[0], nums[1])
            for x in nums[2:]:
                cur = max(prepre + x, pre)
                prepre = pre
                pre = cur
            return pre  # 返回pre而不是cur是考虑到如果只有两家店，那么cur是不存在的

        if not nums: return 0  # 没有店可抢
        if len(nums) == 1: return nums[0]  # 只有一家店可抢
        return max(rob(nums[:-1]), rob(nums[1:]))


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
