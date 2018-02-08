__author__ = 'Hk4Fun'
__date__ = '2018/2/6 23:02'

'''题目描述：
在8*8的国际象棋上摆放八个皇后, 使其不能相互攻击, 即任意两个皇后不得处在同一行, 同一列或者同一对角线上
'''
'''主要思路：
思路1（时间复杂度（O(n!)））：由于8个皇后的任意两个不能处在同一行, 那么肯定每一个皇后占据一行。
       定义一个数组columnIndex[8], 数组中的第i个数字表示位于第i行的皇后列号
       先把数组columnIndex[8]的8个数字分别用0-7初始化, 接下来就是对数组columnIndex的全排列
       因为我们使用不同的数字初始化数组,所以任意两个皇后肯定不同列, 只需判断每一个排列对应的8个皇后是不是在一个对角线上
       也就是对于下标i和j, 是不是 i-j = columnIndex[i]-columnIndex[j] or j-i = columnIndex[i]-columnIndex[j]
思路2：是思路1判断是否处于对角线时的改进，本来是O(n^2)，改进后为O(n)
思路3：思路1和2进行全排列并不是一个有效的算法（暴力枚举），可以使用带剪枝的回溯法，大大降低时间复杂度， 
       参考文章：https://www.cnblogs.com/bigmoyan/p/4521683.html
思路4：递归+位运算, 提高运算速度
       参考文章：http://blog.csdn.net/Dora_Bin/article/details/52733832?locationNum=7
'''

import itertools


class Solution:
    def EightQueen1(self, queenList):
        def is_ok(per):
            for i in range(len(per)):
                for j in range(len(per)):
                    # 由于i和j的对称性，所以只需加一边的abs， 不必abs(i - j) == abs(per[i] - per[j])
                    if i != j and abs(i - j) == per[i] - per[j]:
                        return False
            return True

        if queenList:
            return [per for per in itertools.permutations(queenList) if is_ok(per)]

    def EightQueen2(self, queenList):
        if queenList:
            length = len(queenList)
            result = []
            for per in itertools.permutations(queenList):
                # 处在对角线上的元素，它们的所在位置的行列数值之和或差相等
                # per[i] + i 检测斜率为1的对角线，per[i] - i检测斜率为-1的对角线
                if (length == len(set(per[i] + i for i in range(length)))
                        == len(set(per[i] - i for i in range(length)))):
                    result.append(per)
            return result

    def EightQueen3(self, queenList):
        def is_ok(row):
            for i in range(row):
                # 排除同列和同对角线（斜率+-1），注意这里 row-i一定大于0
                if a_result[row] == a_result[i] or row - i == abs(a_result[row] - a_result[i]):
                    return False
            return True

        def queen(row):
            if row == length:  # 到达最后一行的下一行（已经放置最后一个皇后了），找到了满足条件的序列
                all_result.append(a_result[:])
                return
            for col in range(length):
                a_result[row] = col  # 从第0列开始尝试
                if is_ok(row):  # 剪枝，满足放置条件就进入下一行放置
                    queen(row + 1)  # 进入下一行接着放置（逐行放置皇后）

        if queenList:
            length = len(queenList)
            a_result = [-1] * length  # 初始化一个数组，数组中的第i个数字表示位于第i行的皇后列号
            all_result = []  # 所有满足放置要求的序列
            queen(0)  # 从第0行开始放置
            return all_result

    def EightQueen4(self, queenList):
        def convert(try_bit, row):
            # 将尝试的bit位转换为对应的列号
            for col, bit in enumerate(reversed(bin(try_bit)[2:])):  # 注意要reverse
                if bit == '1':
                    a_result[row] = col
                    return

        def queen(left, mid, right, row):
            if mid == (1 << length) - 1:
                all_result.append(a_result[:])
                return
            allow_bits = ~(left | mid | right) & ((1 << length) - 1)  # &((1 << length) - 1)是为了只保留后面相应长度的比特位
            while allow_bits:
                try_bit = allow_bits & (-allow_bits)  # 取出最右边的'1'
                convert(try_bit, row)
                queen((left | try_bit) << 1, mid | try_bit, (right | try_bit) >> 1, row + 1)
                allow_bits -= try_bit

        if queenList:
            length = len(queenList)
            a_result = [-1] * length
            all_result = []
            queen(left=0, mid=0, right=0, row=0)
            return all_result


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        testArgs.append([range(3), None])

        expected = [(1, 3, 0, 2), (2, 0, 3, 1)]
        testArgs.append([range(4), set(expected)])

        expected = [(0, 2, 4, 1, 3), (0, 3, 1, 4, 2), (1, 3, 0, 2, 4), (1, 4, 2, 0, 3), (2, 0, 3, 1, 4),
                    (2, 4, 1, 3, 0), (3, 0, 2, 4, 1), (3, 1, 4, 2, 0), (4, 1, 3, 0, 2), (4, 2, 0, 3, 1)]
        testArgs.append([range(5), set(expected)])

        expected = [(0, 4, 7, 5, 2, 6, 1, 3), (0, 5, 7, 2, 6, 3, 1, 4), (0, 6, 3, 5, 7, 1, 4, 2),
                    (0, 6, 4, 7, 1, 3, 5, 2), (1, 3, 5, 7, 2, 0, 6, 4), (1, 4, 6, 0, 2, 7, 5, 3),
                    (1, 4, 6, 3, 0, 7, 5, 2), (1, 5, 0, 6, 3, 7, 2, 4), (1, 5, 7, 2, 0, 3, 6, 4),
                    (1, 6, 2, 5, 7, 4, 0, 3), (1, 6, 4, 7, 0, 3, 5, 2), (1, 7, 5, 0, 2, 4, 6, 3),
                    (2, 0, 6, 4, 7, 1, 3, 5), (2, 4, 1, 7, 0, 6, 3, 5), (2, 4, 1, 7, 5, 3, 6, 0),
                    (2, 4, 6, 0, 3, 1, 7, 5), (2, 4, 7, 3, 0, 6, 1, 5), (2, 5, 1, 4, 7, 0, 6, 3),
                    (2, 5, 1, 6, 0, 3, 7, 4), (2, 5, 1, 6, 4, 0, 7, 3), (2, 5, 3, 0, 7, 4, 6, 1),
                    (2, 5, 3, 1, 7, 4, 6, 0), (2, 5, 7, 0, 3, 6, 4, 1), (2, 5, 7, 0, 4, 6, 1, 3),
                    (2, 5, 7, 1, 3, 0, 6, 4), (2, 6, 1, 7, 4, 0, 3, 5), (2, 6, 1, 7, 5, 3, 0, 4),
                    (2, 7, 3, 6, 0, 5, 1, 4), (3, 0, 4, 7, 1, 6, 2, 5), (3, 0, 4, 7, 5, 2, 6, 1),
                    (3, 1, 4, 7, 5, 0, 2, 6), (3, 1, 6, 2, 5, 7, 0, 4), (3, 1, 6, 2, 5, 7, 4, 0),
                    (3, 1, 6, 4, 0, 7, 5, 2), (3, 1, 7, 4, 6, 0, 2, 5), (3, 1, 7, 5, 0, 2, 4, 6),
                    (3, 5, 0, 4, 1, 7, 2, 6), (3, 5, 7, 1, 6, 0, 2, 4), (3, 5, 7, 2, 0, 6, 4, 1),
                    (3, 6, 0, 7, 4, 1, 5, 2), (3, 6, 2, 7, 1, 4, 0, 5), (3, 6, 4, 1, 5, 0, 2, 7),
                    (3, 6, 4, 2, 0, 5, 7, 1), (3, 7, 0, 2, 5, 1, 6, 4), (3, 7, 0, 4, 6, 1, 5, 2),
                    (3, 7, 4, 2, 0, 6, 1, 5), (4, 0, 3, 5, 7, 1, 6, 2), (4, 0, 7, 3, 1, 6, 2, 5),
                    (4, 0, 7, 5, 2, 6, 1, 3), (4, 1, 3, 5, 7, 2, 0, 6), (4, 1, 3, 6, 2, 7, 5, 0),
                    (4, 1, 5, 0, 6, 3, 7, 2), (4, 1, 7, 0, 3, 6, 2, 5), (4, 2, 0, 5, 7, 1, 3, 6),
                    (4, 2, 0, 6, 1, 7, 5, 3), (4, 2, 7, 3, 6, 0, 5, 1), (4, 6, 0, 2, 7, 5, 3, 1),
                    (4, 6, 0, 3, 1, 7, 5, 2), (4, 6, 1, 3, 7, 0, 2, 5), (4, 6, 1, 5, 2, 0, 3, 7),
                    (4, 6, 1, 5, 2, 0, 7, 3), (4, 6, 3, 0, 2, 7, 5, 1), (4, 7, 3, 0, 2, 5, 1, 6),
                    (4, 7, 3, 0, 6, 1, 5, 2), (5, 0, 4, 1, 7, 2, 6, 3), (5, 1, 6, 0, 2, 4, 7, 3),
                    (5, 1, 6, 0, 3, 7, 4, 2), (5, 2, 0, 6, 4, 7, 1, 3), (5, 2, 0, 7, 3, 1, 6, 4),
                    (5, 2, 0, 7, 4, 1, 3, 6), (5, 2, 4, 6, 0, 3, 1, 7), (5, 2, 4, 7, 0, 3, 1, 6),
                    (5, 2, 6, 1, 3, 7, 0, 4), (5, 2, 6, 1, 7, 4, 0, 3), (5, 2, 6, 3, 0, 7, 1, 4),
                    (5, 3, 0, 4, 7, 1, 6, 2), (5, 3, 1, 7, 4, 6, 0, 2), (5, 3, 6, 0, 2, 4, 1, 7),
                    (5, 3, 6, 0, 7, 1, 4, 2), (5, 7, 1, 3, 0, 6, 4, 2), (6, 0, 2, 7, 5, 3, 1, 4),
                    (6, 1, 3, 0, 7, 4, 2, 5), (6, 1, 5, 2, 0, 3, 7, 4), (6, 2, 0, 5, 7, 4, 1, 3),
                    (6, 2, 7, 1, 4, 0, 5, 3), (6, 3, 1, 4, 7, 0, 2, 5), (6, 3, 1, 7, 5, 0, 2, 4),
                    (6, 4, 2, 0, 5, 7, 1, 3), (7, 1, 3, 0, 6, 4, 2, 5), (7, 1, 4, 2, 0, 6, 3, 5),
                    (7, 2, 0, 5, 1, 4, 6, 3), (7, 3, 0, 2, 5, 1, 6, 4)]
        testArgs.append([range(8), set(expected)])

        testArgs.append([None, None])

        return testArgs

    def convert(self, result, *func_arg):
        if result:
            return set([tuple(i) for i in result])


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
