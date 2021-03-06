__author__ = 'Hk4Fun'
__date__ = '2018/1/31 15:58'

'''题目描述：
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵：
[[ 1,  2,  3,  4],
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12],
 [13, 14, 15, 16]]
则依次打印出数字 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''
'''主要思路：
思路1（时间O（n*m）, 空间（1））： 
        由外向内一圈一圈打印，每一圈从左上角开始顺时针打印
        左上角的坐标总是x=y，标记为（start,start）,
        由于每打印一圈，行列都减少2，所以圈数=(min(行，列)+1)//2
        每一圈的打印分四个步骤，且这四个步骤的执行是有条件的，因为里面那一圈并不完整：
        --->    
        ^  |
        |  |    （注意四个步骤的交界处，避免漏或重）
        <--v
        1、从左到右打印一行，条件：当前打印圈的行数>=1且列数>=1（这个条件可以忽略，因为至少要执行第一步）
        2、从上到下打印一列，条件：当前打印圈的行数>=2且列数>=1
        3、从右到左打印一行，条件：当前打印圈的行数>=2且列数>=2
        4、从下到上打印一列，条件：当前打印圈的行数>=3且列数>=2
思路2（时间O（n*m）, 空间（1））：
        上一思路过程繁琐，对边界情况扣的太细了，没有统一的‘模板’，这里给出一个统一的思路：
        一个圈其实只要左上角（startR, startC）和右下角（endR, endC）确定了整个圈也就确定了，
        因此外层循环控制左上角和右下角的变化，内层循环根据这两个坐标分情况绕圈打印就可以了
        外层循环如何控制两个坐标？只需每次让 （startR++, startC++）和 （endR--, endC--）
        什么时候退出？当右下角来到左上角的左上方时退出，换句话讲就是当
        startR <= endR and startC <= endC 时我们才可以进入内层循环打印圈
        那外层循环如何分情况打印圈？情况就三种：
        1、当 startR == endR 时，说明只剩一行
        2、当 startC == endC 时，说明只剩一列
        3、否则为一般情况，绕圈打印即可

思路3（时间O（(m+n)*n*m）, 空间（n*m））： 
        上面的思路是矩阵不动，打印按顺时针，那么可以逆向思维：
        只需从左到右打印矩阵的第一行，然后删除第一行，矩阵逆时针转动
        再从左到右打印矩阵的第一行，以此类推，最后矩阵为空时结束打印
'''


class Solution:
    def PrintMatrix1(self, matrix):
        def PrintMatrixInCircle(matrix, result, cols, rows, start):
            endX = cols + start - 1
            endY = rows + start - 1

            # 从左到右打印一行
            for i in range(start, endX + 1):
                result.append(matrix[start][i])

            # 从上到下打印一列
            if cols >= 1 and rows >= 2:
                for i in range(start + 1, endY + 1):
                    result.append(matrix[i][endX])

            # 从右到左打印一行
            if cols >= 2 and rows >= 2:
                for i in range(endX - 1, start - 1, -1):
                    result.append(matrix[endY][i])

            # 从下到上打印一列
            if cols >= 2 and rows >= 3:
                for i in range(endY - 1, start, -1):
                    result.append(matrix[i][start])

        if not matrix: return
        rows, cols = len(matrix), len(matrix[0])
        result = []
        for start in range((min(rows, cols) + 1) >> 1):
            PrintMatrixInCircle(matrix, result, cols - (start << 1), rows - (start << 1), start)
        return result

    def PrintMatrix2(self, matrix):
        def printEdge(startR, startC, endR, endC):
            if startR == endR:  # 只剩一行
                for col in range(startC, endC + 1):
                    res.append(matrix[startR][col])
            elif startC == endC:  # 只剩一列
                for row in range(startR, endR + 1):
                    res.append(matrix[row][startC])
            else:  # 一般情况
                curR, curC = startR, startC
                while curC != endC:  # 从左到右
                    res.append(matrix[curR][curC])
                    curC += 1
                while curR != endR:  # 从上到下
                    res.append(matrix[curR][curC])
                    curR += 1
                while curC != startC:  # 从右到左
                    res.append(matrix[curR][curC])
                    curC -= 1
                while curR != startR:  # 从下到上
                    res.append(matrix[curR][curC])
                    curR -= 1

        if not matrix: return
        startR, startC, endR, endC = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        res = []
        while startR <= endR and startC <= endC:
            printEdge(startR, startC, endR, endC)
            startR += 1
            startC += 1
            endR -= 1
            endC -= 1
        return res

    def PrintMatrix3(self, matrix):
        def turn(matrix):  # 逆时针旋转矩阵
            if not matrix: return
            matrix_turn = []
            for i in range(len(matrix[0]) - 1, -1, -1):
                row = []
                for j in range(len(matrix)):
                    row.append(matrix[j][i])
                matrix_turn.append(row)
            return matrix_turn

        if not matrix: return
        result = []
        while matrix:
            result += matrix.pop(0)
            matrix = turn(matrix)
        return result


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        def TestMatrix(rows, cols):  # 生成测试用的矩阵
            return [[i * cols + j + 1 for j in range(cols)] for i in range(rows)]

        testArgs = []

        testArgs.append([TestMatrix(1, 1), [1]])
        testArgs.append([TestMatrix(2, 2), [1, 2, 4, 3]])
        testArgs.append([TestMatrix(3, 3), [1, 2, 3, 6, 9, 8, 7, 4, 5]])
        testArgs.append([TestMatrix(4, 4), [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]])
        testArgs.append([TestMatrix(1, 4), [1, 2, 3, 4]])
        testArgs.append([TestMatrix(2, 4), [1, 2, 3, 4, 8, 7, 6, 5]])
        testArgs.append([TestMatrix(3, 4), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]])
        testArgs.append([TestMatrix(4, 1), [1, 2, 3, 4]])
        testArgs.append([TestMatrix(4, 2), [1, 2, 4, 6, 8, 7, 5, 3]])
        testArgs.append([TestMatrix(4, 3), [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]])
        testArgs.append([TestMatrix(0, 0), None])

        return testArgs


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
