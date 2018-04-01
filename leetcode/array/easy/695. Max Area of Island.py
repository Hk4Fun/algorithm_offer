__author__ = 'Hk4Fun'
__date__ = '2018/4/1 0:59'
'''题目描述：
Given a non-empty 2D array grid of 0's and 1's, 
an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.
Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.

Note: The length of each dimension in the given grid does not exceed 50.
'''
'''主要思路：
思路1（时间O（r*c），空间O（r*c））：
DFS(Recursive)
思路2（时间O（r*c），空间O（r*c））：
DFS(Iterative)

递归版虽然没用visited存储访问过的点，而是直接修改原数组，
但用到了栈空间，所以还是O（r*c）。
在某些情况下这样做不被允许，所以在实现迭代版版时乖乖用visited
'''


class Solution:
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    def maxAreaOfIsland_Recursive(self, grid):
        def dfs(grid, r, c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c]:
                grid[r][c] = 0
                return 1 + dfs(grid, r + 1, c) + dfs(grid, r - 1, c) + dfs(grid, r, c + 1) + dfs(grid, r, c - 1)
            return 0

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                res = max(res, dfs(grid, r, c))
        return res

    def maxAreaOfIsland_Iterative(self, grid):
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        res = 0
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val and not visited[r0][c0]:
                    count = 1
                    stack = [(r0, c0)]
                    visited[r0][c0] = True
                    while stack:
                        r, c = stack.pop()
                        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                    and grid[nr][nc] and not visited[nr][nc]):
                                stack.append((nr, nc))
                                visited[nr][nc] = True
                                count += 1
                    res = max(res, count)
        return res


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1000  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
        testArgs.append([grid, 6])

        grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
        testArgs.append([grid, 0])

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
