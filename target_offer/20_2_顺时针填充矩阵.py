__author__ = 'Hk4Fun'
__date__ = '2018/10/8 17:40'
'''题目描述：
给定一个矩阵，从1开始顺时针填充该矩阵
'''
'''主要思路：
顺时针打印矩阵的思路2，只是这里 printEdge 需要返回 nextNum，这样才知道下一圈从哪个数字开始填充
'''


class Solution:
    def buildMatrix(self, matrix):
        def printEdge(nextNum, startR, startC, endR, endC):
            if startR == endR:  # 只剩一行
                for col in range(startC, endC + 1):
                    matrix[startR][col] = nextNum
                    nextNum += 1
            elif startC == endC:  # 只剩一列
                for row in range(startR, endR + 1):
                    matrix[row][startC] = nextNum
                    nextNum += 1
            else:  # 一般情况
                curR, curC = startR, startC
                while curC != endC:  # 从左到右
                    matrix[curR][curC] = nextNum
                    curC += 1
                    nextNum += 1
                while curR != endR:  # 从上到下
                    matrix[curR][curC] = nextNum
                    curR += 1
                    nextNum += 1
                while curC != startC:  # 从右到左
                    matrix[curR][curC] = nextNum
                    curC -= 1
                    nextNum += 1
                while curR != startR:  # 从下到上
                    matrix[curR][curC] = nextNum
                    curR -= 1
                    nextNum += 1
            return nextNum

        if not matrix: return []
        startR, startC, endR, endC = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        nextNum = 1
        while startR <= endR and startC <= endC:
            nextNum = printEdge(nextNum, startR, startC, endR, endC)
            startR += 1
            startC += 1
            endR -= 1
            endC -= 1
        return matrix


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = True  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []

        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        def initMatrix(rows, cols):
            return [[0] * cols for _ in range(rows)]

        testArgs.append([[], []])
        testArgs.append([initMatrix(1, 1), [[1]]])
        testArgs.append([initMatrix(3, 3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]]])
        testArgs.append([initMatrix(2, 3), [[1, 2, 3], [6, 5, 4]]])
        testArgs.append([initMatrix(3, 2), [[1, 2], [6, 3], [5, 4]]])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()
