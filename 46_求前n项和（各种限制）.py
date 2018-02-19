__author__ = 'Hk4Fun'
__date__ = '2018/2/17 23:55'

'''题目描述：
求1+2+3+...+n，
要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''
'''主要思路：
思路1：递归实现，利用and运算的短路原则退出递归
思路2：递归实现，利用模零异常捕获0的情况推出递归
思路3: 递归实现，利用字典进行函数的映射，同时注意到非0值作两次非运算返回True, 0作两次非运算返回False
思路4：利用公式，(n+1)n/2，除2用位运算替代，而乘法可用快速模乘实现
       快速模乘: a = 2^e0 + 2^e1 + 2^e2....
       那么 a * b  = (2^e0 + 2^e1 + 2^e2+...) * b = b * 2^e0 + b * 2^e1 + b * 2^e2 + ...
                   = (b << e0) + (b << e1) + ....
思路5：利用公式，(n+1)n/2 = (n^2+n)/2，除2用位运算替代，乘方调用math中的pow()来替代
思路6：pythonic， 使用sum()
'''


class Solution:
    def Sum1(self, n):
        return n and (n + self.Sum1(n - 1))

    def Sum2(self, n):
        try:
            1 % n  # 模零异常
            return n + self.Sum2(n - 1)
        except ZeroDivisionError:
            return 0

    def Sum3(self, n):
        def sum0(n):
            return 0

        def sumN(n):
            # 此处的func[not not n] 不能写作func[not not n-1], 否则测试用例为0的话会陷入无限递归
            return n + func[not not n](n - 1)

        func = {False: sum0, True: sumN}
        return sumN(n)

    def Sum4(self, n):
        a = n
        b = n + 1
        s = 0
        while a:  # 可以复制32次来替代循环，这里就不这么做了
            # 可以用s += (b & ((a & 1) and (a & 1) ^ 0xfffffffe)) 来替代if
            # 其中 (a & 1) and (a & 1) ^ 0xfffffffe 奇数返回0xffffffff，否则0
            # if a & 1:
            #     s += b
            s += (b & ((a & 1) and (a & 1) ^ 0xfffffffe))
            a >>= 1
            b <<= 1
        return s >> 1

    def Sum5(self, n):
        import math
        return (int(math.pow(n, 2)) + n) >> 1

    def Sum6(self, n):
        return sum(range(1, n + 1))


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        testArgs.append([1, 1])

        testArgs.append([5, 15])

        testArgs.append([10, 55])

        testArgs.append([0, 0])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
