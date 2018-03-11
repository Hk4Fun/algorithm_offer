__author__ = 'Hk4Fun'
__date__ = '2018/2/16 14:52'

'''题目描述：
把n个骰子扔在地上, 所有骰子朝上一面的点数和为s。
输入n, 打印出s的所有可能的值出现的次数（原题要求输出概率，为了方便这里只需输出次数）
'''
'''主要思路： 
思路1：递归实现。设n个骰子投掷点数和为s的出现次数是F(n, s)，
       则F(n, s)等于(n-1)个骰子投掷的点数和为s-1、s-2、s-3、s-4、s-5、s-6时的次数的总和：
       即 F(n, s) = F(n - 1, s - 1) + F(n - 1, s - 2) + F(n - 1, s - 3) 
                  + F(n - 1, s - 4) + F(n - 1, s - 5) + F(n - 1, s - 6)。
       所有的和出现次数总和为6^n，概率为F(n, s)/6^n。(n <= s <= 6*n)
思路2：循环实现。由于递归实现复杂度高（重复计算），采用上述思路的循环实现
'''


class Solution:
    # 输出要求：比如返回[(1,5),(2,5)]，表示和为1的出现次数为5，和为2的出现次数为5
    def DicesProbability1(self, n):
        def count(n, s):
            if s < n or s > 6 * n:  # n <= s <= 6*n
                return 0
            if n == 1:  # 只有一个骰子时和为s的次数只有一次
                return 1
            return count(n - 1, s - 1) + count(n - 1, s - 2) + count(n - 1, s - 3) \
                   + count(n - 1, s - 4) + count(n - 1, s - 5) + count(n - 1, s - 6)

        if not n or n < 1:
            return
        return [(s, count(n, s)) for s in range(n, 6 * n + 1)]

    def DicesProbability2(self, n):
        if not n or n < 1:
            return
        maxVal = 6
        count = [[0] * (maxVal * n + 1), []]  # 构造两个数组来存放每一个和出现的次数，下标表示和，里面的值代表次数
        flag = 0  # 用flag来反复利用这两个数组
        for i in range(1, maxVal + 1):  # 一开始只有一个骰子，当然次数都为1
            count[flag][i] = 1
        for i in range(2, n + 1):  # 逐渐加入其他骰子
            # 一开始另一个数组要初始化为0，因为每加入一个骰子就会使前面的和次数成为0
            # 比如，先是1个骰子时和为1的次数为1，当加入第二个骰子时，和为1是不可能出现的
            # 换句话说，就是和的范围是动态变化的，且一直往右移
            count[1 - flag] = [0] * (maxVal * n + 1)
            for j in range(i, maxVal * i + 1):  # i <= s <= 6*i
                k = 1
                while k <= j and k <= maxVal:
                    # F(n, s) = F(n - 1, s - 1) + F(n - 1, s - 2) + F(n - 1, s - 3)
                    #         + F(n - 1, s - 4) + F(n - 1, s - 5) + F(n - 1, s - 6)
                    count[1 - flag][j] += count[flag][j - k]
                    k += 1
            flag = 1 - flag  # 将flag更新，flag永远指向求和好的数组
        return [(i, count[flag][i]) for i in range(n, maxVal * n + 1)]


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        testArgs.append([0, None])

        testArgs.append([1, [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1)]])

        testArgs.append([2, [(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6),
                             (8, 5), (9, 4), (10, 3), (11, 2), (12, 1)]])

        testArgs.append([3, [(3, 1), (4, 3), (5, 6), (6, 10), (7, 15), (8, 21),
                             (9, 25), (10, 27), (11, 27), (12, 25), (13, 21),
                             (14, 15), (15, 10), (16, 6), (17, 3), (18, 1)]])

        testArgs.append([4, [(4, 1), (5, 4), (6, 10), (7, 20), (8, 35), (9, 56),
                             (10, 80), (11, 104), (12, 125), (13, 140), (14, 146),
                             (15, 140), (16, 125), (17, 104), (18, 80), (19, 56),
                             (20, 35), (21, 20), (22, 10), (23, 4), (24, 1)]])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
