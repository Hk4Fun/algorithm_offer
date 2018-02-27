__author__ = 'Hk4Fun'
__date__ = '2018/2/27 16:09'

'''题目描述：
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，
每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''
'''主要思路：
思路1：回溯法。
       1.从(0,0)开始走，先判断四个方向是否满足条件，满足就把相应位置标记为True，
       再递归，最终统计有几处标记为True
       2.判断当前节点是否可达的标准为：
       1）当前节点在矩阵内；
       2）当前节点未被访问过；
       3）当前节点满足limit限制。
       注意，这里不是寻找路径，而是类似于扫雷，
       走过的地方发现满足条件就算作能够到达，走不下去了也不必回退
       注意这里若去遍历所有位置看是否满足条件是不行的，因为有可能出现单个‘孤岛’或者是连在一起的‘孤岛’，
       即这些位置虽然满足条件，但四周并不满足条件，这样机器人是无法到达这些位置的
思路2：将思路1改成非递归，多一个栈实现。对比两种写法的异同，体会递归和迭代互改的套路
'''


class Solution:
    def movingCount1(self, threshold, rows, cols):
        def canReach(row, col, threshold):
            sum = 0
            while row or col:
                sum += row % 10 + col % 10
                row //= 10
                col //= 10
            return sum <= threshold

        def movingCountCore(threshold, rows, cols, row, col, visited):
            for i, j in [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]:
                if 0 <= i < rows and 0 <= j < cols \
                        and canReach(i, j, threshold) \
                        and not visited[i * cols + j]:  # 先判断四个方向是否满足条件
                    visited[i * cols + j] = True
                    movingCountCore(threshold, rows, cols, i, j, visited)

        if threshold == None or threshold < 0 or not cols or not rows:
            return 0
        visited = [False] * (rows * cols)
        visited[0] = True
        movingCountCore(threshold, rows, cols, 0, 0, visited)  # 从（0，0）开始移动
        return sum(visited)

    def movingCount2(self, threshold, rows, cols):
        def canReach(row, col, threshold):
            sum = 0
            while row or col:
                sum += row % 10 + col % 10
                row //= 10
                col //= 10
            return sum <= threshold

        if threshold == None or threshold < 0 or not cols or not rows:
            return 0
        visited = [False] * (rows * cols)
        visited[0] = True
        stack = [(0, 0)]  # 递归中传的是坐标，所以压栈时应压坐标，这里先压(0, 0)表示从（0, 0）开始移动
        while stack:  # 递归改迭代的外循环控制
            row, col = stack.pop()  # 模拟进入函数时的弹栈，弹出参数
            for i, j in [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]:
                if 0 <= i < rows and 0 <= j < cols \
                        and canReach(i, j, threshold) \
                        and not visited[i * cols + j]:
                    visited[i * cols + j] = True
                    stack.append((i, j))  # 模拟调用函数时的压栈，压入参数
        return sum(visited)


# ================================测试代码================================


from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug模式下每个测试用例只测试一遍，默认情况下关闭debug模式
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([8, 11, 11, 45])
        testArgs.append([5, 10, 10, 21])
        testArgs.append([15, 20, 20, 359])
        testArgs.append([15, 30, 30, 759])
        testArgs.append([10, 1, 100, 29])
        testArgs.append([10, 1, 10, 10])
        testArgs.append([15, 100, 1, 79])
        testArgs.append([15, 10, 1, 10])
        testArgs.append([15, 1, 1, 1])
        testArgs.append([-10, 10, 10, 0])
        testArgs.append([None, None, None, 0])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
