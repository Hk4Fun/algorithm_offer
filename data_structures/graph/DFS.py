__author__ = 'Hk4Fun'
__date__ = '2018/3/15 21:15'
'''
深度优先搜索（邻接表时间O(V+E)，邻接矩阵时间O(V^2)）：
类似于二叉树的前序遍历，用一个visited数组来标记访问过的顶点，避免重复访问
'''


class Solution:
    def dfs_recursion(self, graph, start):
        '''
        递归实现
        :param graph: 图的邻接表
        :param start: 遍历的起始顶点
        :return: list，按顺序遍历过的顶点的值
        '''

        def dfs(graph, start):
            visited.add(start)
            res.append(start)
            for next in graph[start] - visited:
                dfs(graph, next)

        res = []
        visited = set()
        dfs(graph, start)
        return res

    def dfs_iteration(self, graph, start):
        '''
        非递归实现
        :param graph: 图的邻接表
        :param start: 遍历的起始顶点
        :return: list，按顺序遍历过的顶点的值
        '''
        stack, res, visited = [start], [], set()
        while stack:
            cur = stack.pop()
            res.append(cur)
            visited.add(cur)
            for next in graph[cur] - visited:
                stack.append(next)
        return res


# ================================测试代码================================


from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 10000  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        a, b, c, d, e = range(5)
        graph = [{b, c}, {a, d}, {a, d}, {e}, {a}]
        testArgs.append([graph, a, ([a, b, d, e, c], [a, c, d, e, b])])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected[0] or result == expected[1]


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
