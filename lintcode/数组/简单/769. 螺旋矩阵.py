__author__ = 'Hk4Fun'
__date__ = '2018/3/25 19:43'
'''题目描述：
给出整数 n, 返回一个大小为 n * n 的螺旋矩阵

样例:
给出 n = 3 
则螺旋矩阵为:
[
[1,2,3]
[8,9,4]
[7,6,5]
]
'''
'''主要思路：

'''


class Solution:
    """
    @param n: a Integer
    @return: a spiral array
    """
    def spiralArray(self, n):
        def PrintMatrixInCircle(matrix, cols, rows, start, count):
            endX = cols + start - 1
            endY = rows + start - 1

            # 从左到右打印一行
            for i in range(start, endX + 1):
                matrix[start][i] = count
                count += 1

            # 从上到下打印一列
            if cols >= 1 and rows >= 2:
                for i in range(start + 1, endY + 1):
                    matrix[i][endX] = count
                    count += 1

            # 从右到左打印一行
            if cols >= 2 and rows >= 2:
                for i in range(endX - 1, start - 1, -1):
                    matrix[endY][i] = count
                    count += 1

            # 从下到上打印一列
            if cols >= 2 and rows >= 3:
                for i in range(endY - 1, start, -1):
                    matrix[i][start] = count
                    count += 1
            return count

        matrix = [[0] * n for _ in range(n)]
        rows = cols = n
        count = 1
        for start in range((min(rows, cols) + 1) >> 1):
            count = PrintMatrixInCircle(matrix, cols - (start << 1), rows - (start << 1), start, count)
        return matrix


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

        matrix = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]
        ]
        testArgs.append([3, matrix])

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
