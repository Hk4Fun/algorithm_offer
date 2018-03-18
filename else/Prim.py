__author__ = 'Hk4Fun'
__date__ = '2018/3/16 1:03'
'''
Prim算法（时间O(n^2)，空间O(n)）：
可在加权连通无向图里搜索最小生成树，即由此算法搜索到的边所构成的树中，
不但包括了连通图里的所有顶点，且其所有边的权值之和最小。
从图中任意取出一个顶点把它当成一棵树，然后从与这棵树相接的边中选取一条最短（权值最小）的边，
并将这条边及其所连的顶点也并入这棵树中，此时得到了一棵有两个顶点的树。
然后从与这棵树相接的边中选取一条最短的边，并将这条边及其所连顶点并入当前树中，
得到一棵有3个顶点的树，以此类推，直到图中所有顶点被并入树中为止，此时得到的生成树就是最小生成树

注意：
1、Prim算法针对加权连通无向图
2、在构造最小生成树的过程中权值相等的候选边都被并入生成树的图，其最小生成树唯一
3、从不同顶点出发构造最小生成树时并入树中的顶点顺序会不一样，当最终的最小生成树是一样的（最小生成树唯一的话）
4、时间复杂度为O(n^2)，可见Prim算法只与图的顶点数量有关而与边数无关，因此Prim算法适用于稠密图
'''


class Solution:
    def Prim(self, graph, start):
        '''
        Prim算法实现最小生成树（MST）
        :param graph: 图的邻接矩阵
        :param start: 生成树的起始顶点
        :return: 最小生成树的边，最小权重。其中最小生成树的边放入集合返回且每条边也是集合，表示成顶点对。
        '''
        num = len(graph)  # 顶点数量
        low_cost = [graph[start][i] for i in range(num)]  # 当前生成树到剩余各顶点最短边的权值，初始化为起始点到各点权值
        add_node = [False] * num  # 标记某顶点是否加入当前生成树
        add_node[start] = True  # 起始点加入当前生成树
        pair_node = [start] * num  # 记录与加入顶点配对的顶点，两顶点间的边就是加入生成树的边，初始化为起始点
        edges = set()  # 返回加入生成树的边，其实顶点不一样生成顺序会不一样，但最后加入的边都一样（如果生成树唯一的话）
        sum = 0  # 最小生成树的总权值

        for i in range(num - 1):
            min = 1 << 20  # 这里不能float('inf')， 因为graph中已经出现，而float('inf')-1等于float('inf')
            for j in range(num):  # 选出候选边的最小者，即选出当前生成树到其余顶点最短边的最小值
                if not add_node[j] and low_cost[j] < min:
                    min = low_cost[j]
                    next = j
            add_node[next] = True  # 加入当前生成树

            # 以下两行代码可以根据需求改变而实现不同的功能，如统计权重、记录加入的边等
            sum += min
            # set中只能加入不可变对象，而set本身是可变对象，所以要使用不可变的集合对象，即frozenset
            edges.add(frozenset({pair_node[next], next}))  # 把边加入当前生成树，注意Prim算法是一种无向图算法

            for j in range(num):  # 以刚加入的顶点next为媒介更新候选边
                if not add_node[j] and graph[next][j] < low_cost[j]:
                    low_cost[j] = graph[next][j]
                    pair_node[j] = next  # 记录候选边的配对顶点
        return edges, sum


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
        for i in range(len(graph)):  # 顺便验证注意点3
            testArgs.append([graph, i, ({edge1, edge2, edge3, edge4}, 8)])

        graph = [[0, 12, 16, 18, _],
                 [12, 0, 2, _, 22],
                 [16, 2, 0, 4, _],
                 [18, _, 4, 0, 10],
                 [_, 22, _, 10, 0]]
        edge1 = frozenset({0, 1})
        edge2 = frozenset({1, 2})
        edge3 = frozenset({2, 3})
        edge4 = frozenset({3, 4})
        for i in range(len(graph)):
            testArgs.append([graph, i, ({edge1, edge2, edge3, edge4}, 28)])

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
