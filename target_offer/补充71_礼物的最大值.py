__author__ = 'Hk4Fun'
__date__ = '2018/3/5 13:58'

'''题目描述：
在一个m*n的棋盘的每一个格都放有一个礼物，每个礼物都有一定价值（大于0）。
从左上角开始拿礼物，每次向右或向下移动一格，直到右下角结束。
给定一个棋盘，求拿到礼物的最大价值。例如，对于如下棋盘：
1    10   3    8
12   2    9    6
5    7    4    11
3    7    16   5
礼物的最大价值为1+12+5+7+7+16+5=53。
'''
'''主要思路：
动态规划（时间O(m*n),空间O(n)）:
定义函数f(i,j)表示到达坐标为(i,j)的格子时能拿到的礼物总和的最大值。
根据题目要求，有两种可能的途径到达坐标为(i,j)的格子：通过格子(i,j-1)或(i-1,j)。
即来自左边格子或上边格子。故状态转移方程为：f(i,j) = max(f(i-1,j),f(i,j-1))+gift[i,j]
gift[i,j]表示坐标为(i,j)的格子里礼物的价值。
优化：由于礼物的最大价值只依赖坐标为(i-1,j)和(i,j-1)的两个格子，
因此第i-1行及更上面的格子礼物的最大价值实际上不必保存下来。所以可以用一个一维数组作备忘。
有两种遍历方式：行优先遍历，即自左向右，自上而下；列优先遍历，自上而下，自左向右。
这两种方式都保证了在求f(i,j)时已经求出了f(i-1,j)和f(i,j-1)。
注意边界情况：第一行没有来自上边的格子，第一列没有来自左边的格子
'''


class Solution:
    def getMaxValue(self, values):
        if not values: return 0
        cols = len(values[0])
        dp = [0] * cols
        for i in range(len(values)):
            for j in range(cols):
                dp[j] = max(dp[j], dp[j - 1] if j > 0 else 0) + values[i][j]
        return dp[-1]


# ================================测试代码================================


from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug模式下每个测试用例只测试一遍，默认情况下关闭debug模式
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 29])
        testArgs.append([[[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]], 53])
        testArgs.append([[[1, 10, 3, 8]], 22])
        testArgs.append([[[1], [12], [5], [3]], 21])
        testArgs.append([[[3]], 3])
        testArgs.append([None, 0])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
