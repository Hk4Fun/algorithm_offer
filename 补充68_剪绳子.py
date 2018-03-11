__author__ = 'Hk4Fun'
__date__ = '2018/3/4 0:15'

'''题目描述：
给你一根长度为n的绳子，请把绳子剪成m段，记每段绳子长度为k[0],k[1]...k[m-1],求k[0]k[1]...k[m-1]的最大值。
已知绳子长度n为整数，n>1且m>1(至少要剪一刀，不能不剪)，k[0],k[1]...k[m-1]均要求为整数。
例如，绳子长度为8时，把它剪成3-3-2，得到最大乘积18；绳子长度为3时，把它剪成2-1，得到最大乘积2。
'''
'''主要思路：
思路1： 动态规划（时间O(n^2)，空间O(n)）。
        定义函数f(n)为把长度为n的绳子剪成若干段后各段长度乘积的最大值。
        则状态转移方程为：f(n)= max(f(i)*f(n-i)),其中0<i<n。考虑边界情况：
        当n=2时，f(2)=1; 当n=3时，f(3)=2。递归实现会发生重复计算，所以这里自下而上计算
        （从上往下分析问题，从下往上求解问题，用一维或二维数组作备忘录）
思路2： 贪心（时间O(1)，空间O(1)）。
        当n>=5时，尽可能多地剪长度为3的绳子；当剩下的绳子长度为4时，把绳子剪成两段长度为2的绳子
        （需要数学证明该贪心策略可以取到最优解，不具有通用性，具体证明见第二版书P98）
'''


class Solution:
    def cuttingRope1(self, length):
        if length == None:
            return
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2
        dp = [0] * (length + 1)
        dp[1], dp[2], dp[3] = 1, 2, 3  # 注意边界值的填写

        for i in range(4, length + 1):
            max = 0
            for j in range(1, (i >> 1) + 1):
                mul = dp[j] * dp[i - j]
                if mul > max:
                    max = mul
                dp[i] = max
        return dp[length]


    def cuttingRope2(self, length):
        if not length:
            return
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2

        numOf3 = length // 3
        if length - numOf3 * 3 == 1:
            numOf3 -= 1
        numOf2 = (length - numOf3 * 3) >> 1
        return (3 ** numOf3) * (2 ** numOf2)


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = True  # debug模式下每个测试用例只测试一遍，默认情况下关闭debug模式
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([1, 0])
        testArgs.append([2, 1])
        testArgs.append([3, 2])
        testArgs.append([4, 4])
        testArgs.append([5, 6])
        testArgs.append([6, 9])
        testArgs.append([7, 12])
        testArgs.append([8, 18])
        testArgs.append([9, 27])
        testArgs.append([10, 36])
        testArgs.append([50, 86093442])
        testArgs.append([None, None])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
