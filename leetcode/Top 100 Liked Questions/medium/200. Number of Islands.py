__author__ = 'Hk4Fun'
__date__ = '2018/8/12 17:04'
'''题目描述：
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''
'''主要思路：
思路1：union_find (quick-union)

思路2：dfs（连在一起的全部消掉（置为0），类似消消乐）

'''


class Solution:
    """
    :type grid: List[List[str]]
    :rtype: int
    """

    def numIslands1(self, grid):
        def find(p):
            while self.id[p] != p:
                p = self.id[p]
            return p

        def union(p, q):  # quick-union
            pid, qid = find(p), find(q)
            if pid == qid: return
            self.id[pid] = qid
            self.count -= 1

        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        self.count = rows * cols
        self.id = list(range(rows * cols))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    p = i * cols + j
                    if i - 1 >= 0 and grid[i - 1][j] == '1':
                        union(p, (i - 1) * cols + j)
                    if i + 1 < rows and grid[i + 1][j] == '1':
                        union(p, (i + 1) * cols + j)
                    if j - 1 >= 0 and grid[i][j - 1] == '1':
                        union(p, i * cols + (j - 1))
                    if j + 1 < cols and grid[i][j + 1] == '1':
                        union(p, i * cols + (j + 1))
                else:  # 0不是岛屿，前面 self.count=rows*cols 全算进去了，这里减回来
                    self.count -= 1
        return self.count

    def numIslands2(self, grid):
        def dfs(i, j):
            if 0 <= i < rows and 0 <= j < cols and grid[i][j] == '1':
                grid[i][j] = '0' # 消掉该岛屿
                # 消掉周围相连的岛屿，注意这里必须用list来启动map（否则只返回一个生成器），py2下可以不用list
                list(map(dfs, (i, i, i - 1, i + 1), (j - 1, j + 1, j, j)))
                return 1
            return 0

        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        return sum(dfs(i, j) for i in range(rows) for j in range(cols))


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

        testArgs.append([[["1", "1", "1", "1", "0"],
                          ["1", "1", "0", "1", "0"],
                          ["1", "1", "0", "0", "0"],
                          ["0", "0", "0", "0", "0"]], 1])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()
