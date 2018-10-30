__author__ = 'Hk4Fun'
__date__ = '2018/8/21 19:37'
'''题目描述：
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''
'''主要思路：
target_offer/66_矩阵中的路径.py
'''


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def dfs(i, j, pathlen):
            if pathlen == len(word): return True
            haspath = False
            if 0 <= i < rows and 0 <= j < cols and not visited[i][j] and word[pathlen] == board[i][j]:
                visited[i][j] = True
                haspath = dfs(i - 1, j, pathlen + 1) or \
                          dfs(i + 1, j, pathlen + 1) or \
                          dfs(i, j - 1, pathlen + 1) or \
                          dfs(i, j + 1, pathlen + 1)
                if not haspath: visited[i][j] = False  # 记得回溯
            return haspath

        rows, cols = len(board), len(board[0])
        visited = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False


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

        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()
