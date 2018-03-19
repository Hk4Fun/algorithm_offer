__author__ = 'Hk4Fun'
__date__ = '2018/3/19 12:56'
'''
Dijkstra算法（时间O（n^2），空间O（n））：
找出指定顶点到其他各顶点的最短路径——单源最短路径
不能解决负权值边的图

对比Dijkstra算法和Prim算法，会发现其代码结构十分相似，区别就在于
Prim算法：graph[next][j] < low_cost[j]
Dijkstra算法：dist[next] + graph[next][j] < dist[j]
Prim只是从边中选更短，而Dijkstra还要进行累加看是否更短
因为Prim算法求的是树的最小权重，不管之前的权重到底累加到多少了，只管选择最短路径；
而Dijkstra算法求的是最短路径，具有累加性，是在原来的路径上累加，需要顾及之前到顶点路径的最短长度
'''


class Solution:
    def Dijkstra(self, graph, start):
        '''
        Dijkstra算法，找出指定顶点到其他各顶点的最短路径
        :param graph: 图的邻接矩阵
        :param start: 指定的起始顶点
        :return: 起始顶点到其他各顶点的最短路径及其对应的路径长度
        '''

        def findPath(end):  # 返回从起始顶点到指定终点的路径
            stack = []
            while path[end] != -1:  # 使用栈逆向寻找路径
                stack.insert(0, end)
                end = path[end]
            stack.insert(0, end)
            return stack

        def Dijkstra():
            add_node = [False] * num  # 标记顶点是否已经并入最短路径
            add_node[start] = True  # V0并入最短路径中
            # dist表示当前已找到的从V0到Vi的最短路径的长度。
            # 初态：V0到Vi的权重
            dist = [graph[start][i] for i in range(num)]
            # path保存从V0到Vi最短路径上Vi的前一个顶点，为打印路径准备。
            # 初态：如果V0到Vi有边，则path[Vi]=V0，否则path[Vi]=-1
            path = [start if graph[start][i] < float('inf') else -1 for i in range(num)]
            path[start] = -1

            for i in range(num):
                min = 1 << 32
                for j in range(num):  # 从通往各顶点的最短路径中选出最小值
                    if not add_node[j] and dist[j] < min:
                        next = j
                        min = dist[j]
                add_node[next] = True  # 并入选出的顶点
                for j in range(num):  # 以选中的顶点为中转站，判断该顶点的加入是否会出现比原来通往其他顶点更短的路径
                    # 进入松弛操作
                    if not add_node[j] and dist[next] + graph[next][j] < dist[j]:
                        dist[j] = dist[next] + graph[next][j]  # 更新为更短的路径
                        path[j] = next  # 更新到其他顶点的前一顶点为刚刚选中的顶点
            return dist, path

        num = len(graph)  # 顶点数量
        dist, path = Dijkstra()
        return [(findPath(i), dist[i]) for i in range(1, num)]


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

        _ = float('inf')
        graph = [[0, 4, 6, 6, _, _, _],
                 [_, 0, 1, _, 7, _, _],
                 [_, _, 0, _, 6, 4, _],
                 [_, _, 2, 0, _, 5, _],
                 [_, _, _, _, 0, _, 6],
                 [_, _, _, _, 1, 0, 8],
                 [_, _, _, _, _, _, 0]]
        expected = [([0, 1], 4), ([0, 1, 2], 5), ([0, 3], 6), ([0, 1, 2, 5, 4], 10),
                    ([0, 1, 2, 5], 9), ([0, 1, 2, 5, 4, 6], 16)]
        testArgs.append([graph, 0, expected])

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
