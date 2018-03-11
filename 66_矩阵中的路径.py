__author__ = 'Hk4Fun'
__date__ = '2018/2/27 14:07'

'''题目描述：
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
例如 [[a b c e], 
      [s f c s], 
      [a d e e]] 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
'''
'''主要思路：
思路1：回溯法，用一个状态数组保存之前访问过的字符位置，然后再分别按上，下，左，右递归
思路2：思路1的优化
'''


class Solution:
    def hasPath1(self, matrix, rows, cols, path):
        def hasPathCore(row, col, pathLength, visited):
            if len(path) == pathLength:  # 来到末尾，成功找到路径
                return True
            hasPath = False
            if 0 <= row < rows and 0 <= col < cols \
                    and matrix[row * cols + col] == path[pathLength] \
                    and not visited[row * cols + col]:
                pathLength += 1
                visited[row * cols + col] = True
                hasPath = hasPathCore(row, col - 1, pathLength, visited) or \
                          hasPathCore(row - 1, col, pathLength, visited) or \
                          hasPathCore(row, col + 1, pathLength, visited) or \
                          hasPathCore(row + 1, col, pathLength, visited)
                if not hasPath:  # 上下左右都没找到路径，则回退
                    pathLength -= 1
                    visited[row * cols + col] = False
            return hasPath

        if not matrix or not rows or not cols or not path or rows < 1 or cols < 1:
            return False
        visited = [False] * (rows * cols)  # 访问过的字符位置置1
        pathLength = 0
        for row in range(rows):  # 遍历以每个格子作为开头的路径
            for col in range(cols):
                if hasPathCore(row, col, pathLength, visited):
                    return True
        return False

    def hasPath2(self, matrix, rows, cols, path):
        def visit(steps, matrix, rows, cols, path):
            if len(steps) == len(path):
                return True
            i, j = steps[-1]
            next_steps = [(ii, jj) for ii, jj in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]
                          if 0 <= ii < rows and 0 <= jj < cols and (ii, jj) not in steps
                          and matrix[ii * cols + jj] == path[len(steps)]]
            return sum([visit(steps + [step], matrix, rows, cols, path) for step in next_steps])

        if not matrix or not rows or not cols or not path or rows < 1 or cols < 1:
            return False
        for i, s in enumerate(matrix):
            if s == path[0] and visit([(i // cols, i % cols)], matrix, rows, cols, path):
                return True
        return False


# ================================测试代码================================


from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = True  # debug模式下每个测试用例只测试一遍，默认情况下关闭debug模式
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        # ABCE
        # SFCS
        # ADEE

        # ABCCED
        testArgs.append(['ABCESFCSADEE', 3, 4, 'ABCCED', True])
        # SEE
        testArgs.append(['ABCESFCSADEE', 3, 4, 'SEE', True])
        # ABCB
        testArgs.append(['ABCESFCSADEE', 3, 4, 'ABCB', False])

        # ABCEHJIG
        # SFCSLOPQ
        # ADEEMNOE
        # ADIDEJFM
        # VCEIFGGS

        # SLHECCEIDEJFGGFIE
        testArgs.append(['ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS', 5, 8, 'SLHECCEIDEJFGGFIE', True])
        # SGGFIECVAASABCEHJIGQEM
        testArgs.append(['ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS', 5, 8, 'SGGFIECVAASABCEHJIGQEM', True])
        # SGGFIECVAASABCEEJIGOEM
        testArgs.append(['ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS', 5, 8, 'SGGFIECVAASABCEEJIGOEM', False])
        # SGGFIECVAASABCEHJIGQEMS
        testArgs.append(['ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS', 5, 8, 'SGGFIECVAASABCEHJIGQEMS', False])

        # AAAA
        # AAAA
        # AAAA

        # AAAAAAAAAAAA
        testArgs.append(['AAAAAAAAAAAA', 3, 4, 'AAAAAAAAAAAA', True])
        # AAAAAAAAAAAAA
        testArgs.append(['AAAAAAAAAAAA', 3, 4, 'AAAAAAAAAAAAA', False])

        # A

        # A
        testArgs.append(['A', 1, 1, 'A', True])
        # B
        testArgs.append(['A', 1, 1, 'B', False])

        testArgs.append([None, None, None, None, False])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
