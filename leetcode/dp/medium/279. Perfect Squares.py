__author__ = 'Hk4Fun'
__date__ = '2018/4/5 14:28'
'''题目描述：
Given a positive integer n, find the least number of perfect square numbers 
(for example, 1, 4, 9, 16, ...) which sum to n.
For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, 
return 2 because 13 = 4 + 9.
'''
'''主要思路：
思路1：dp
dp[i]表示i的最少平方数，
则 dp[i] = 1 if i 为平方数否则 dp[i] = min(dp[j * j] + dp[i - j * j], while j * j < i) 

思路2：bfs
http://ox186n2j0.bkt.clouddn.com/bfs.png

思路3：Lagrange 四平方定理 和 Lagrange 三平方定理
https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem
https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem
Lagrange 四平方定理告诉我们：
任何自然数都可以由4个平方数组成，即 n = a^2 + b^2 + c^2 + d^2，所以这题的答案已经限定在了[1,4]；
而Lagrange 三平方定理又告诉我们：
满足n=(4^a)(8b+7)的自然数一定由4个平方数组成，不满足该式的自然数由3个平方数组成
所以该题可以用排除法完成：
判断一个数最少可以由一个平方数还是两个平方数组成很简单，剩下的如果满足n=(4^a)(8b+7)，
则一定只能由4个平方数组成，不满足的就由3个平方数组成
'''


class Solution:
    """
    :type n: int
    :rtype: int
    """

    def numSquares_dp(self, n):  # Time Limit Exceeded
        if n <= 1: return n
        dp = [0, 1]
        for i in range(2, n + 1):
            minV = float('inf')
            j = 1
            while j * j < i:
                minV = min(dp[j * j] + dp[i - j * j], minV)
                j += 1
            dp.append(1 if j * j == i else minV)
        return dp[-1]

    def numSquares_bfs(self, n):  # Accepted 220ms
        if n <= 1: return n
        l, i = [], 1
        while i * i <= n:
            l.append(i * i)
            i += 1
        bfs, level = {n}, 0
        while bfs:
            level += 1
            tmp = set()
            for x in bfs:
                for y in l:
                    if x == y:
                        return level
                    if x < y:
                        break
                    tmp.add(x - y)
            bfs = tmp

    def numSquares_Lagrange(self, n):  # Accepted 56ms
        # Based on Lagrange's Four Square theorem, there are only 4 possible results: 1, 2, 3, 4.
        def is_square(n):
            return int(n ** 0.5) * int(n ** 0.5) == n

        if n <= 1: return n
        if is_square(n): return 1  # If n is a perfect square, return 1.
        for i in range(1, int((n ** 0.5) + 1)):  # Check whether 2 is the result.
            if is_square(n - i * i):
                return 2
        # The result is 4 if and only if n can be written in the form of 4^k*(8*m + 7).
        # Please refer to Legendre's three-square theorem.
        while (n & 3) == 0: n >>= 2  # while n%4 == 0: n//4
        if n & 7 == 7: return 4  # n%8 == 7
        return 3


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

        testArgs.append([0, 0])
        testArgs.append([1, 1])
        testArgs.append([2, 2])
        testArgs.append([3, 3])
        testArgs.append([4, 1])
        testArgs.append([5, 2])
        testArgs.append([6, 3])
        testArgs.append([7, 4])
        testArgs.append([8, 2])
        testArgs.append([9, 1])
        testArgs.append([6337, 2])

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
