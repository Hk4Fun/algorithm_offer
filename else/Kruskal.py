__author__ = 'Hk4Fun'
__date__ = '2018/3/19 11:33'
'''
Kruskal算法（时间O（eloge），空间O（n））：
将图中的边按权值从小到大排序，然后从最小的边开始扫描，并检测当前边是否为候选边，
即是否改变的并入会构成回路，如不构成回路，则将该边并入当前生成树中，直到所有边都被检测完为止
判断是否生成回路要用到并查集，可用来查找边的两个顶点是否在同一集合，同一集合说明并入后会产生回路，
不同一集合就可以并入，然后将它们放在同一集合。
'''


class edge:
    def __init__(self, a, b, w):
        self.a = a
        self.b = b
        self.w = w


class Solution:
    def Kruskal(self, graph, vertex_num):
        '''
        Kruskal算法实现最小生成树（MST）
        :param graph: 图的所有边，object of class edge
        :param vertex_num: 图的顶点数量
        :return: 最小生成树的边，最小权重
        '''

        def findHead(a):  # 在并查集中查找头结点
            while a != father[a]:
                a = father[a]
            return a

        edge_num = len(graph)
        father = list(range(vertex_num))  # 一开始每个顶点的头结点为自己
        graph = sorted(graph, key=lambda x: x.w)  # 按照边的权重排序， 时间复杂度eloge
        edges = set()  # 最小生成树的边
        sum = 0  # 最小生成树的权重
        for i in range(edge_num):
            a, b = findHead(graph[i].a), findHead(graph[i].b)
            if a != b:  # 边的两个顶点不在同一集合，未成环，可以并入生成树
                father[a] = b  # 合并两个顶点所在的集合
                edges.add(graph[i])
                sum += graph[i].w
        return edges, sum


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

        edge0 = edge(0, 1, 5)
        edge1 = edge(0, 2, 1)
        edge2 = edge(0, 3, 2)
        edge3 = edge(1, 2, 3)
        edge4 = edge(2, 3, 6)
        edge5 = edge(1, 4, 4)
        edge6 = edge(2, 4, 2)
        edge7 = edge(3, 4, 3)
        graph = [edge0, edge1, edge2, edge3, edge4, edge5, edge6, edge7]
        testArgs.append([graph, 5, ({edge1, edge2, edge3, edge6}, 8)])

        edge0 = edge(0, 1, 12)
        edge1 = edge(0, 2, 16)
        edge2 = edge(0, 3, 18)
        edge3 = edge(1, 2, 2)
        edge4 = edge(2, 3, 4)
        edge5 = edge(1, 4, 22)
        edge6 = edge(2, 4, 10)
        graph = [edge0, edge1, edge2, edge3, edge4, edge5, edge6]
        testArgs.append([graph, 5, ({edge0, edge3, edge4, edge6}, 28)])

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
