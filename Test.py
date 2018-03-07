__author__ = 'Hk4Fun'
__date__ = '2018/2/4 16:55'

import traceback
import timeit
import inspect
import copy

TEST_NUM = 10000  # 单个测试用例的测试次数


class Test:
    def __init__(self, solution):
        self.solution = solution  # 解题实例
        self.pass_num = 0  # 通过测试的数量
        self.time_pool = []  # 耗时
        self.debug = False  # debug模式下每个测试用例只测试一遍，默认情况下关闭debug模式
        self.methods = list(filter(inspect.ismethod, (getattr(solution, name) for name in dir(solution))))  # 解题方法列表

    def print_runtime(self, time):  # time单位：μs
        if time < 1000:
            print('Average Runtime：{:.2f}μs\n'.format(time))
        elif time < 1000000:
            print('Average Runtime：{:.2f}ms\n'.format(time / 1000))
        else:
            print('Average Runtime：{:.2f}s\n'.format(time / 1000000))

    def test(self, test_name, method_num, expected, *func_arg):
        # method_num 表示要测试的解题方法序号
        print('{} begins:'.format(test_name))

        try:
            total_time = 0
            result = None
            for i in range(1 if self.debug else TEST_NUM):
                func_arg_copy = copy.deepcopy(func_arg)
                start = timeit.default_timer()
                result = self.methods[int(method_num) - 1](*func_arg_copy)
                end = timeit.default_timer()
                total_time += end - start
            result = self.convert(result, *func_arg)
        except Exception:
            print('Failed: Syntax Error！')
            print(traceback.format_exc())
            return

        if result == expected:
            average_runtime = (total_time / (1 if self.debug else TEST_NUM)) * 1000000
            print('Passed.')
            self.print_runtime(average_runtime)
            self.pass_num += 1
            self.time_pool.append(average_runtime)
        else:
            print('Failed: The test does not pass！')
            print('Test for: {}'.format(func_arg))
            print('Your result: {}\nBut expected: {}\n'.format(result, expected))

    def start_test(self):
        runtime = {}  # 各解题思路的耗时
        for i, method in enumerate(self.methods):
            self.pass_num = 0
            self.time_pool = []
            testArgs = self.my_test_code()
            test_num = len(testArgs)  # 总的测试数量
            for j, testArg in enumerate(testArgs):
                testName = "Test" + str(i + 1) + "_" + str(j + 1)
                self.test(testName, i + 1, testArg[-1], *tuple(testArg[:-1]))
            print('Result of Testing {}: {} / {}, {:.2f}%'.format(method.__name__,
                                                                  self.pass_num, test_num,
                                                                  (self.pass_num / test_num) * 100))
            if self.pass_num:
                time = sum(self.time_pool) / self.pass_num
                print('Total ', end='')
                self.print_runtime(time)
                if self.pass_num == test_num:  # 通过全部测试才加入排行版进行排名
                    runtime[method.__name__] = round(time, 2)
            print('*' * 100)
        print('Runtime Ranking (unit：μs, test_num: {})：\n{}'.format(1 if self.debug else TEST_NUM,
                                                                    sorted(runtime.items(), key=lambda x: x[1]),
                                                                    ))

    def my_test_code(self):
        # 只需在此处填写测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        testArgs = []
        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result
