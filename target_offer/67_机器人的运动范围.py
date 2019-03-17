__author__ = 'Hk4Fun'
__date__ = '2018/2/27 16:09'

'''题目描述：
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，
每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''
'''主要思路：
典型的DFS
1.从(0,0)开始走，先判断四个方向是否满足条件，满足就把相应位置标记为True，
再递归，最终统计有几处标记为True
2.判断当前节点是否可达的标准为：
1）当前节点在矩阵内；
2）当前节点未被访问过；
3）当前节点满足题目要求。
注意，这里不是寻找路径，而是类似于扫雷，
走过的地方发现满足条件就算作能够到达，走不下去了也不必回退
注意这里若去遍历所有位置看是否满足条件是不行的，因为有可能出现单个‘孤岛’或者是连在一起的‘孤岛’，
即这些位置虽然满足条件，但四周并不满足条件，这样机器人是无法到达这些位置的
除了使用 visited 数组标记访问过的位置，还可以进行剪枝：
由于我们从 (0, 0) 出发，因此整体的遍历方向是向右和向下的，不必向左向上遍历
'''


class Solution:
    def movingCount1(self, threshold, rows, cols):
        def canReach(row, col):
            sum = 0
            while row or col:
                sum += row % 10 + col % 10
                row //= 10
                col //= 10
            return sum <= threshold

        def movingCountCore(row, col, visited):
            for i, j in [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]:
                if 0 <= i < rows and 0 <= j < cols \
                        and canReach(i, j) \
                        and not visited[i * cols + j]:  # 先判断四个方向是否满足条件
                    visited[i * cols + j] = True
                    movingCountCore(i, j, visited)

        if threshold is None or threshold < 0 or not cols or not rows:
            return 0
        visited = [False] * (rows * cols)
        visited[0] = True
        movingCountCore(0, 0, visited)  # 从（0，0）开始移动
        return sum(visited)

    def movingCount(self, threshold, rows, cols):
        def can_reach(i, j):
            sum = 0
            while i or j:
                sum += i % 10 + j % 10
                i //= 10
                j //= 10
            return sum <= threshold

        def search(i, j):
            if 0 <= i < rows and 0 <= j < cols and not visited[i][j] and can_reach(i, j):
                # 注意这里and判断条件的顺序，必须先判断 i, j 的有效性，否则直接访问 visited 数组有可能越界
                # 而且把 can_reach 放最后判断，减少重复计算
                visited[i][j] = True
                # search(i - 1, j) # 剪枝
                search(i + 1, j)
                # search(i, j - 1) # 剪枝
                search(i, j + 1)

        if threshold is None or threshold < 0 or not cols or not rows: return 0
        visited = [[False] * cols for _ in range(rows)]
        search(0, 0)
        return sum(sum(row) for row in visited)


# ================================测试代码================================


from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = True  # debug模式下每个测试用例只测试一遍，默认情况下关闭debug模式
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
