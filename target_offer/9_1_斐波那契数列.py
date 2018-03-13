__author__ = 'Hk4Fun'
__date__ = '2018/1/3 23:07'

'''题目描述：
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项f(n)
（n从0开始，f(0)=0，f(1)=1）
'''
'''主要思路：
思路1：非线性递归，简洁但效率低，O(2^n)
思路2：线性递归，O(n)
思路3：尾递归，O(n)
思路4：循环，一般解法，O(n)
思路5：生成器，pythonic，O(n)
思路6：矩阵，转化成矩阵的乘方，然后用递归，实现代码量大，不实用，O(logn)
思路7：公式法，最直接暴力，这里不实现，O(1)
'''


class Solution:
    def Fibonacci1(self, n):  # 非线性递归
        return n if n <= 1 else self.Fibonacci1(n - 1) + self.Fibonacci1(n - 2)

    def Fibonacci2(self, n):  # 线性递归
        def fib(a, b, n):
            return 1 if n == 1 else a + fib(b, a + b, n - 1)

        return n if n <= 1 else fib(0, 1, n)

    def Fibonacci3(self, n):  # 尾递归
        def fib(a, b, n):
            return a if n == 0 else fib(b, a + b, n - 1)

        return n if n <= 1 else fib(0, 1, n)

    def Fibonacci4(self, n):
        tempArray = [0, 1]
        if n >= 2:
            for i in range(2, n + 1):
                tempArray[i & 1] = tempArray[0] + tempArray[1]  # 注意这里 i&1 的巧妙
        return tempArray[n & 1]

    def Fibonacci5(self, n):
        def fib(n):
            a, b = 0, 1
            for i in range(n + 1):
                yield a
                a, b = b, a + b

        return [i for i in fib(n)][n]

    def Fibonacci6(self, n):
        def MatrixMultipy(matrix1, matrix2):
            # result = []
            # for i in range(len(matrix1)):
            #     row = []
            #     for j in range(len(matrix2[0])):
            #         col = 0
            #         for k in range(len(matrix1[0])):
            #             col += matrix1[i][k] * matrix2[k][j]
            #         row.append(col)
            #     result.append(row)
            # return result
            # 由于这里的矩阵乘法固定2*2，所以可以直接运算返回，不用遍历
            return [[matrix1[0][0] * matrix2[0][0] + matrix1[0][1] * matrix2[1][0],
                     matrix1[0][0] * matrix2[0][1] + matrix1[0][1] * matrix2[1][1]],
                    [matrix1[1][0] * matrix2[0][0] + matrix1[1][1] * matrix2[1][0],
                     matrix1[1][0] * matrix2[0][1] + matrix1[1][1] * matrix2[1][1]]]

        def MatrixPower(n):
            if n == 1:
                return [[1, 1], [1, 0]]
            elif n % 2 == 0:
                matrix = MatrixPower(n // 2)
                return MatrixMultipy(matrix, matrix)
            elif n % 2 == 1:
                matrix = MatrixPower((n - 1) // 2)
                matrix = MatrixMultipy(matrix, matrix)
                return MatrixMultipy(matrix, [[1, 1], [1, 0]])

        if n <= 1:
            return n
        return MatrixPower(n - 1)[0][0]


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        testArgs = []
        testArgs.append([0, 0])
        testArgs.append([1, 1])
        testArgs.append([2, 1])
        testArgs.append([3, 2])
        testArgs.append([4, 3])
        testArgs.append([5, 5])
        testArgs.append([6, 8])
        testArgs.append([7, 13])
        testArgs.append([8, 21])
        testArgs.append([9, 34])
        testArgs.append([10, 55])
        # testArgs.append([20, 6765])

        return testArgs


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
