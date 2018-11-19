__author__ = 'Hk4Fun'
__date__ = '2018/8/6 18:51'
'''题目来源:
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
'''
'''题目描述：

'''
'''主要思路：
思路1：递归+缓存

思路2：一维dp
先使用数学思路，可以知道赋予标号后，集合中包含负数和正数，
则有 sum(Positive)-sum(Negtive) = S
因为sum(Positive)+sum(Negtive)=sum(nums)，
则有2*sum(Positive)=sum(nums)+S，
故sum(Positive)=(sum(nums)+S)/2，
由于(sum(nums)+S)/2是固定的整数，所以只要从nums中找到和为(sum(nums)+S)/2的组合数即可。
经过上述解析，可以将问题转化为从nums中找到和为(sum(nums)+S)/2的组合个数。
这个问题可以通过dp来解决，用dp[i][j]表示nums中前i项和为j的组合数，
则dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]] (0<=i<len(nums),nums[i]<=j<=(sum(nums)+S)/2)
其中dp[i-1][j]表示不选择第i项，那么组合数就是前i-1项和为j的组合数
dp[i-1][j-nums[i]]表示选择第i项，则组合数为前i-1项和为j-nums[i]的组合数
如果 j-nums[i]<0，则dp[i-1][j-nums[i]]=0，即 dp[i][j] = dp[i-1][j]
注意到dp[i]只与dp[i-1]，即只与上一层有关，因此优化空间后为：
dp[i] = dp[i] + dp[i-nums[i]]，从右往左填充一维表格（滚动数组）
'''


class Solution:
    """
    :type nums: List[int]
    :type S: int
    :rtype: int
    """

    def findTargetSumWays1(self, nums, S):
        def findsum(n, cursum):
            if (n, cursum) not in dp:
                res = 0
                if n == len(nums):
                    if cursum == S:
                        res = 1
                else:
                    add = findsum(n + 1, cursum + nums[n])
                    sub = findsum(n + 1, cursum - nums[n])
                    res = add + sub
                dp[(n, cursum)] = res
            return dp[(n, cursum)]

        dp = {}
        return findsum(0, 0)

    def findTargetSumWays2(self, nums, S):
        s = sum(nums)
        if s < S: return 0
        if (S + s) % 2 == 1: return 0
        target = (S + s) // 2
        dp = [1] + [0] * target # 注意初始状态的设定
        for num in nums:
            for i in range(target, num - 1, -1): # 注意i的左边界为num，否则i-num越界
                dp[i] = dp[i] + dp[i - num]
        return dp[target]


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

        testArgs.append([[1, 1, 1, 1, 1], 3, 5])
        # testArgs.append([[1, 1], 0, 2])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()
