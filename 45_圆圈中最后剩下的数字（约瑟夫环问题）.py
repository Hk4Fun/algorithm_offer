__author__ = 'Hk4Fun'
__date__ = '2018/2/17 22:48'

'''题目描述：
0, 1, 2, n-1这n个数字排成一个圆环, 从数字0开始每次从这个圆圈里删除第m个数字
求这个圆圈中最后剩下的一个数字。
'''
'''主要思路：
思路1（时间O(mn)，空间O(n)）：
经典解法，用环形链表模拟整个删除过程
思路2（时间O(n)，空间O(1)）：
推导递归公式。定义f(n,m)表示每次在n个数字0，1，...，n-1中每次删除第m个数字最后剩下的数字，则有递归公式：
         0               ,n=1
f(n,m)={                        ，具体推导过程直接看书P230~231
         [f(n-1,m)+m]%n  ,n>1
'''


class Solution:
    def LastRemaining1(self, n, m):
        if not n or not m:
            return -1
        circle = list(range(n))
        last = 0
        while len(circle) > 1:
            last = (last + m - 1) % len(circle)
            circle.pop(last)
        return circle[0]

    # 循环实现
    def LastRemaining2(self, n, m):
        if not n or not m:
            return -1
        last = 0
        for i in range(2, n + 1):
            last = (last + m) % i
        return last

    # 递归实现
    def LastRemaining3(self, n, m):
        import sys
        sys.setrecursionlimit(5000)  # 设置最大递归深度
        def last(n, m):
            if n == 1:
                return 0
            return (last(n - 1, m) + m) % n

        if not n or not m:
            return -1
        return last(n, m)


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        testArgs.append([5, 3, 3])

        testArgs.append([5, 2, 2])

        testArgs.append([6, 7, 4])

        testArgs.append([6, 6, 3])

        testArgs.append([0, 0, -1])

        testArgs.append([4000, 997, 1027])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
