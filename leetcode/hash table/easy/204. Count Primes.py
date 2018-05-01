__author__ = 'Hk4Fun'
__date__ = '2018/5/1 12:05'
'''题目描述：
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''
'''主要思路：
注： 0和1不是素数

思路1：暴力，检查每个数是否为素数（超时TLE）
思路2：哈希表，快速筛法
思路3：思路2的简化，外层循环遍历的终点是根号n而不是n
      内层循环（切片）筛选的起点是i*i,而不是i*1，可以避免重复筛选
'''


class Solution:
    """
    :type n: int
    :rtype: int
    """

    def countPrimes1(self, n):
        def is_prime(n):
            s = 2
            while s ** 2 <= n:
                if n % s == 0: return False
                s += 1
            return True

        if n < 3: return 0
        count = 0
        for i in range(2, n):
            if is_prime(i): count += 1
        return count

    def countPrimes2(self, n):
        is_prime = [True] * n  # 初始化认为所有数都为素数
        count = 0
        for i in range(2, n):  # 0和1不是素数
            if is_prime[i]:
                count += 1
                j = 1
                while i * j < n:
                    is_prime[i * j] = False
                    j += 1
        return count

    def countPrimes3(self, n):
        if n < 3: return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):  # 外层循环终点是根号n
            if is_prime[i]:
                is_prime[i * i: n: i] = [False] * len(is_prime[i * i: n: i])  # 内层循环的起点为i*i
        return sum(is_prime)


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

        testArgs.append([499979, 41537])

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
