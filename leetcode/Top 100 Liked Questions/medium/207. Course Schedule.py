__author__ = 'Hk4Fun'
__date__ = '2018/8/13 11:31'
'''题目描述：
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, 
for example to take course 0 you have to first take course 1, 
which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, 
is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, 
             and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. 
You may assume that there are no duplicate edges in the input prerequisites.
'''
'''主要思路：
拓扑排序算法
'''

from collections import defaultdict


class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0] * numCourses  # 结点入度
        outside = defaultdict(set)  # 出边表
        for i, j in prerequisites:
            indegree[i] += 1
            outside[j].add(i)
        # 入度为0的结点作为拓扑排序的起始结点
        stack = [node for node, ind in enumerate(indegree) if ind == 0]
        while stack:
            node = stack.pop()
            for neigh in outside[node]:  # 将该结点的所有出边结点的入度减一
                indegree[neigh] -= 1
                if indegree[neigh] == 0:  # 将入度为0的结点加入拓扑排序
                    stack.append(neigh)
        return sum(indegree) == 0  # 最终所有结点的入度应该为0


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

        testArgs.append([2, [[1, 0]], True])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()
