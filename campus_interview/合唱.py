__author__ = 'Hk4Fun'
__date__ = '2018/8/28 17:53'
'''题目来源:
网易2018校园招聘第7题
'''
'''题目描述：
小Q和牛博士合唱一首歌曲,这首歌曲由n个音调组成,每个音调由一个正整数表示。
对于每个音调要么由小Q演唱要么由牛博士演唱,对于一系列音调演唱的难度等于所有相邻音调变化幅度之和, 
例如一个音调序列是8, 8, 13, 12, 那么它的难度等于|8 - 8| + |13 - 8| + |12 - 13| = 6(其中||表示绝对值)。
现在要对把这n个音调分配给小Q或牛博士,让他们演唱的难度之和最小,请你算算最小的难度和是多少。
如样例所示: 小Q选择演唱{5, 6}难度为1, 牛博士选择演唱{1, 2, 1}难度为2,难度之和为3,这一个是最小难度和的方案了。

Input

输入包括两行,第一行一个正整数n(1 ≤ n ≤ 2000) 第二行n个整数vi, 表示每个音调。

Output

输出一个整数,表示小Q和牛博士演唱最小的难度和是多少。

Sample Input

5
1 5 6 2 1

Sample Output

3
'''
'''主要思路：
正推, 容易想到一个人继续演唱或换人演唱的时候发生状态转移：

设 dp[i][j] 表示当前小Q唱到第 i 个音调，牛博士唱到第 j 个音调的难度和；
不妨设当前 i > j ：
若 i - 1 == j 则发生换人，由于不知道上一次 i 唱到哪里，状态由 min{ dp[k][j] + abs(v[i] - v[k]) }, k < j 转移来；
若 i - 1 > j 则表示当前是从 i - 1 唱到 i 的，没有换人，状态由 dp[i-1][j] + abs(v[i] - v[i-1]) 累加；
不妨设 dp[i][j] 表示当前演唱到第 i 个，上一个人演唱到第 j 个，则状态转移方程为

dp[i][j] = dp[i-1][j] + abs(v[i] - v[i-1]), j < i - 1
dp[i][i -1] = min{ dp[i-1][k] + abs(v[i] - v[k]) }, k < i - 1

边界情况是一个人唱第一个，后面所有音调让另一个人唱
dp[i][0] = dp[i-1][0] + abs(v[i] - v[i-1]), i ≥ 2

或者一个人唱前面所有音调，最后一个音调让另一个人唱
dp[i][i-1] = dp[i-1][i-2] + abs(v[i-1] - v[i-2]), i ≥ 2 (注意，这里是v[i-1]不是v[i])
'''


class Solution:
    def chorus(self, nums):
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(2, n):
            dp[i][i - 1] = dp[i - 1][i - 2] + abs(nums[i - 1] - nums[i - 2])
        for i in range(2, n):
            for j in range(i - 1):
                dp[i][j] = dp[i - 1][j] + abs(nums[i] - nums[i - 1])
                dp[i][i - 1] = min(dp[i][i - 1], dp[i - 1][j] + abs(nums[i] - nums[j]))
        return min(dp[-1][:-1])


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

        testArgs.append([[1, 5, 6, 2, 1], 3])
        testArgs.append([[5, 5, 4, 4], 0])
        testArgs.append([[24, 13, 2, 4, 54, 23, 12, 53, 12, 23, 42, 13, 53,
                          12, 24, 12, 11, 24, 42, 52, 12, 32, 42], 188])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()
