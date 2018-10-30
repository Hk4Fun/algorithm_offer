__author__ = 'Hk4Fun'
__date__ = '2018/8/9 9:58'
'''题目描述：
Given a char array representing tasks CPU need to do. 
It contains capital letters A to Z where different letters represent different tasks.
Tasks could be done without original order. 
Each task could be done in one interval. 
For each interval, CPU could finish one task or just be idle.
However, there is a non-negative cooling interval n that means between two same tasks, 
there must be at least n intervals that CPU are doing different tasks or just be idle.
You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
'''
'''主要思路：
时间O（n），空间O（1）
https://leetcode.com/problems/task-scheduler/solution/
Approach #3 Calculating Idle slots
这里用py实现，思路基本一致
当idle_slots不够时，tasks本身不需要依靠idle就可以达到要求的interval
'''

from collections import Counter


class Solution:
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """

    def leastInterval1(self, tasks, n):
        mapper = [0] * 26
        for c in tasks:
            mapper[ord(c) - ord('A')] += 1
        max_val = max(mapper) - 1
        idle_slots = max_val * n
        for v in mapper:
            idle_slots -= min(v, max_val)
        idle_slots += max_val  # 多减了一次max_val（本身）
        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)

    def leastInterval2(self, tasks, n):  # 简化版
        task_count = tuple(Counter(tasks).values())
        m = max(task_count)
        mc = task_count.count(m)
        return max((m - 1) * (n + 1) + mc, len(tasks))


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

        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()
