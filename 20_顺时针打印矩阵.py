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
由外向内一圈一圈打印，每一圈从左上角开始顺时针打印
左上角的坐标总是x=y，标记为（start,start）,
画图分析找规律可知：当 cols > start * 2 and rows > start * 2 时可以继续往内打印
每一圈的打印分四个步骤进行，且这四个步骤的执行是有条件的，因为里面那一圈并不完整：
--->    
^  |
|  |    （注意四个步骤的交界处，避免漏或重）
<--v
1、从左到右打印一行，条件：当前打印圈的行数>=1且列数>=1（这个条件可以忽略，因为至少要执行第一步）
2、从上到下打印一列，条件：当前打印圈的行数>=2且列数>=1
3、从右到左打印一行，条件：当前打印圈的行数>=2且列数>=2
4、从下到上打印一列，条件：当前打印圈的行数>=3且列数>=2
'''


class Solution:
    # matrix类型为二维列表，需要返回列表
    def PrintMatrix(self, matrix):
        if not matrix:
            return
        rows = len(matrix)
        cols = len(matrix[0])
        if rows == 0 or cols == 0:
            return
        l = []

        start = 0
        while (cols > start * 2 and rows > start * 2):
            self.PrintMatrixInCircle(matrix, l, cols - start * 2, rows - start * 2, start)
            start += 1
        return l

    def PrintMatrixInCircle(self, matrix, l, cols, rows, start):
        endX = cols + start - 1
        endY = rows + start - 1

        # 从左到右打印一行
        for i in range(start, endX + 1):
            l.append(matrix[start][i])

        # 从上到下打印一列
        if cols >= 1 and rows >= 2:
            for i in range(start + 1, endY + 1):
                l.append(matrix[i][endX])

        # 从右到左打印一行
        if cols >= 2 and rows >= 2:
            for i in range(endX - 1, start - 1, -1):
                l.append(matrix[endY][i])

        # 从下到上打印一列
        if cols >= 2 and rows >= 3:
            for i in range(endY - 1, start, -1):
                l.append(matrix[i][start])


# ================================测试代码================================
import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 总的测试数量
time_pool = []  # 耗时


def Test(testName, matrix, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    test = Solution()
    try:
        start = timeit.default_timer()
        result = test.PrintMatrix(matrix)
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


def TestMatrix(rows, cols):  # 生成测试用的矩阵
    return [[i * cols + j + 1 for j in range(cols)] for i in range(rows)]


Test('Test1', TestMatrix(1, 1), [1])
Test('Test2', TestMatrix(2, 2), [1, 2, 4, 3])
Test('Test3', TestMatrix(3, 3), [1, 2, 3, 6, 9, 8, 7, 4, 5])
Test('Test4', TestMatrix(4, 4), [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])
Test('Test5', TestMatrix(1, 4), [1, 2, 3, 4])
Test('Test6', TestMatrix(2, 4), [1, 2, 3, 4, 8, 7, 6, 5])
Test('Test7', TestMatrix(3, 4), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
Test('Test8', TestMatrix(4, 1), [1, 2, 3, 4])
Test('Test9', TestMatrix(4, 2), [1, 2, 4, 6, 8, 7, 5, 3])
Test('Test10', TestMatrix(4, 3), [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8])
Test('Test11', TestMatrix(0, 0), None)

print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))
