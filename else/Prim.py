__author__ = 'Hk4Fun'
__date__ = '2018/3/16 1:03'
'''

'''


class Solution:
    def prim(self, graph, start):
        num = len(graph)  # 顶点数量
        low_cost = [graph[start][i] for i in range(num)]  # 当前生成树到剩余各顶点最短边的权值，初始化为起始点到各点权值
        add_node = [False] * num  # 标记某顶点是否加入当前生成树
        add_node[start] = True  # 起始点加入当前生成树
        pair_node = [start] * num  # 记录与加入顶点配对的顶点，两顶点间的边就是加入生成树的边，初始化为起始点
        res = set()  # 返回按顺序加入生成树的边
        sum = 0  # 最小生成树的总权值

        for i in range(num - 1):
            min = 1 << 20
            for j in range(num):
                if not add_node[j] and low_cost[j] < min:
                    min = low_cost[j]
                    next = j
            add_node[next] = True
            sum += min
            res.add(frozenset({pair_node[next], next}))
            for j in range(num):
                if not add_node[j] and graph[next][j] < low_cost[j]:
                    low_cost[j] = graph[next][j]
                    pair_node[j] = next
        return res, sum


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        _ = float('inf')

        graph = [[0, 5, 1, 2, _],
                 [5, 0, 3, _, 4],
                 [1, 3, 0, 6, 2],
                 [2, _, 6, 0, 3],
                 [_, 4, 2, 3, 0]]
        edge1 = frozenset({0, 2})
        edge2 = frozenset({0, 3})
        edge3 = frozenset({2, 4})
        edge4 = frozenset({2, 1})
        for i in range(len(graph)):
            testArgs.append([graph, i, ({edge1, edge2, edge3, edge4}, 8)])

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
