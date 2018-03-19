__author__ = 'Hk4Fun'
__date__ = '2018/3/19 20:53'
'''
Bellman-Ford算法（时间O（VE））：
Bellman-Ford算法（下文中简称为BF）与Dijkstra算法一样，解决的是单源最短路径问题。
两者不同之处在于，后者只适用于无负权边的图，而BF无此限制：只要图中没有负权环，
则该算法可以正确地给出起点到其余各点的最短路径，否则报告负权环的存在。
'''


class Solution:
    def bellman_ford(self, G, s):
        '''
        :param G: 图的带权字典（类似邻接表）
        :param s: 起始顶点
        :return:若不含负权环则返回D, P，否则返回False
        '''

        def relax(G, u, v, D, P):  # 松弛操作
            old = D.get(v, float('inf'))  # 若D[v]不存在则返回inf
            new = D.get(u, float('inf')) + G[u][v]
            if new < old:
                D[v], P[v] = new, u
                return True  # 若有改进，则返回True
            return False

        D, P = {s: 0}, {s: None}
        for _ in G:  # 轮数等于顶点数
            change = False
            for u in G:
                for v in G[u]:  # 遍历所有的边
                    if relax(G, u, v, D, P):
                        change = True
            if not change:  # 如果某轮没有任何松弛
                break  # 说明所有的最短路径已经松弛结束，退出循环
        else:  # 否则，正常跳出循环，说明第n轮也有松弛，存在负权环
            return False
        return D, P


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

        s, t, x, y, z = range(5)
        G = {
            s: {t: 6, y: 7},
            t: {x: 5, y: 8, z: -4},
            x: {t: -2},
            y: {x: -3, z: 9},
            z: {s: 2, x: 7}
        }
        testArgs.append([G, s, ({s: 0, t: 2, x: 4, y: 7, z: -2}, {s: None, t: x, x: y, y: s, z: t})])

        G = {
            s: {t: -100, y: 7},  # 含有负权环
            t: {x: 5, y: 8, z: -4},
            x: {t: -2},
            y: {x: -3, z: 9},
            z: {s: 2, x: 7}
        }
        testArgs.append([G, s, False])

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
