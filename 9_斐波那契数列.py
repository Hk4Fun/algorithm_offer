__author__ = 'Hk4Fun'
__date__ = '2018/1/3 23:07'

'''题目描述：
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项f(n)
（n从0开始，f(0)=0，f(1)=1）
'''
'''主要思路：
思路1：递归，简洁但效率低，O(n^2)
思路2：循环，一般解法，O(n)
思路3：生成器，pythonic，O(n)
思路4：矩阵，转化成矩阵的乘方，然后用递归，实现代码量大，不实用，O(logn)
思路5：公式法，最直接暴力，这里不实现，O(1)
'''


class Solution:
    def Fibonacci1(self, n):
        if n <= 1:
            return n
        return self.Fibonacci1(n - 1) + self.Fibonacci1(n - 2)

    def Fibonacci2(self, n):
        tempArray = [0, 1]
        if n >= 2:
            for i in range(2, n + 1):
                tempArray[i % 2] = tempArray[0] + tempArray[1]  # 注意这里 i%2 的巧妙
        return tempArray[n % 2]

    def Fibonacci3(self, n):
        def fib(n):
            a, b = 0, 1
            for i in range(n + 1):
                yield a
                a, b = b, a + b

        return [i for i in fib(n)][n]

    def Fibonacci4(self, n):
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

import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 中的测试数量
time_pool = []  # 耗时


def Test(testName, method_type, n, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    test = Solution()
    result = None
    start = end = 0
    try:
        if method_type == 1:
            start = timeit.default_timer()
            result = test.Fibonacci1(n)
            end = timeit.default_timer()
        elif method_type == 2:
            start = timeit.default_timer()
            result = test.Fibonacci2(n)
            end = timeit.default_timer()
        elif method_type == 3:
            start = timeit.default_timer()
            result = test.Fibonacci3(n)
            end = timeit.default_timer()
        elif method_type == 4:
            start = timeit.default_timer()
            result = test.Fibonacci4(n)
            end = timeit.default_timer()
    except Exception as e:
        print('Failed:语法错误！')
        print(traceback.format_exc())
        return
    if (result == expected):
        print('Passed.\n')
        pass_num += 1
        time_pool.append(end - start)
    else:
        print('Failed:测试不通过！\n')


# Test('Test1_1', 1, 0, 0)
# Test('Test1_2', 1, 1, 1)
# Test('Test1_3', 1, 2, 1)
# Test('Test1_4', 1, 3, 2)
# Test('Test1_5', 1, 4, 3)
# Test('Test1_6', 1, 5, 5)
# Test('Test1_7', 1, 6, 8)
# Test('Test1_8', 1, 7, 13)
# Test('Test1_9', 1, 8, 21)
# Test('Test1_10', 1, 9, 34)
# Test('Test1_11', 1, 10, 55)
# Test('Test1_12', 1, 20, 6765)

Test('Test2_1', 2, 0, 0)
Test('Test2_2', 2, 1, 1)
Test('Test2_3', 2, 2, 1)
Test('Test2_4', 2, 3, 2)
Test('Test2_5', 2, 4, 3)
Test('Test2_6', 2, 5, 5)
Test('Test2_7', 2, 6, 8)
Test('Test2_8', 2, 7, 13)
Test('Test2_9', 2, 8, 21)
Test('Test2_10', 2, 9, 34)
Test('Test2_11', 2, 10, 55)
Test('Test2_12', 2, 40, 102334155)

# Test('Test3_1', 3, 0, 0)
# Test('Test3_2', 3, 1, 1)
# Test('Test3_3', 3, 2, 1)
# Test('Test3_4', 3, 3, 2)
# Test('Test3_5', 3, 4, 3)
# Test('Test3_6', 3, 5, 5)
# Test('Test3_7', 3, 6, 8)
# Test('Test3_8', 3, 7, 13)
# Test('Test3_9', 3, 8, 21)
# Test('Test3_10', 3, 9, 34)
# Test('Test3_11', 3, 10, 55)
# Test('Test3_12', 3, 40, 102334155)

# Test('Test4_1', 4, 0, 0)
# Test('Test4_2', 4, 1, 1)
# Test('Test4_3', 4, 2, 1)
# Test('Test4_4', 4, 3, 2)
# Test('Test4_5', 4, 4, 3)
# Test('Test4_6', 4, 5, 5)
# Test('Test4_7', 4, 6, 8)
# Test('Test4_8', 4, 7, 13)
# Test('Test4_9', 4, 8, 21)
# Test('Test4_10', 4, 9, 34)
# Test('Test4_11', 4, 10, 55)
# Test('Test4_12', 4, 40, 102334155)

print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
if pass_num:
    print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))
