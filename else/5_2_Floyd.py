__author__ = 'Hk4Fun'
__date__ = '2018/3/19 15:48'
'''
Floyd算法（时间O（n^3），空间O（n^2））：
求出任意两点间的最短路径————全局最短路径
'''


class Solution:
    def Floyd(self, graph):
        '''
        Floyd算法求出任意两点间的最短路径及其长度
        :param graph: 图的邻接矩阵
        :return: 返回任意两点的最短路径及其长度
        '''

        def findPath(start, end):  # 根据path递归查找start到end的路径
            def find(start, end):
                if path[start][end] == -1:  # 直连，没有中转点
                    res.append(start)
                else:
                    mid = path[start][end]  # 找到中转顶点
                    find(start, mid)  # 寻找start到中转点的路径
                    find(mid, end)  # 寻找中转点到end的路径

            res = []
            find(start, end)
            return res + [end]

        def floyd(graph):
            from copy import deepcopy
            A, path = deepcopy(graph), [[-1] * num for i in range(num)]

            for k in range(num):
                for i in range(num):
                    for j in range(num):
                        if A[i][j] > A[i][k] + A[k][j]:
                            A[i][j] = A[i][k] + A[k][j]
                            path[i][j] = k
            return A, path  # A中保存任意两点的最短路径长度，path保存任意两点的中转点，-1表示直连

        num = len(graph)
        A, path = floyd(graph)
        res = []
        for i in range(num):  # 找到任意两点的最短路径及其长度
            for j in range(num):
                res.append((findPath(i, j), A[i][j]))
        return res


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 100  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        _ = float('inf')
        graph = [[0, 5, _, 7],
                 [_, 0, 4, 2],
                 [3, 3, 0, 2],
                 [_, _, 1, 0]]
        expected = [([0, 0], 0),
                    ([0, 1], 5),
                    ([0, 3, 2], 8),
                    ([0, 3], 7),
                    ([1, 3, 2, 0], 6),
                    ([1, 1], 0),
                    ([1, 3, 2], 3),
                    ([1, 3], 2),
                    ([2, 0], 3),
                    ([2, 1], 3),
                    ([2, 2], 0),
                    ([2, 3], 2),
                    ([3, 2, 0], 4),
                    ([3, 2, 1], 4),
                    ([3, 2], 1),
                    ([3, 3], 0), ]
        testArgs.append([graph, expected])

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
