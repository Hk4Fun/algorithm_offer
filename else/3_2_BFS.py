__author__ = 'Hk4Fun'
__date__ = '2018/3/15 23:15'
'''
广度优先搜索（邻接表时间O(V+E)，邻接矩阵时间O(V^2)）：
类似于二叉树的层序遍历，但与二叉树的层序遍历有些不同：访问结点后才入队，不能反过来，否则会重复访问
用一个visited数组来标记访问过的顶点，避免重复访问

'''


class Solution:
    def bfs(self, graph, start):
        '''
        非递归实现
        :param graph: 图的邻接表
        :param start: 遍历的起始顶点
        :return: list，按顺序遍历过的顶点的值
        '''
        res = []
        visited = set()
        res.append(start)
        visited.add(start)
        queue = [start]
        while queue:
            cur = queue.pop(0)
            for next in graph[cur] - visited:
                res.append(next)  # 访问结点后才入队，不能反过来，否则会重复访问
                visited.add(next)
                queue.append(next)
        return res


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = True  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 100  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        a, b, c, d, e = range(5)
        graph = [{b, c}, {a, d}, {a, d}, {e}, {a}]
        testArgs.append([graph, a, [a, b, c, d, e]])

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
