__author__ = 'Hk4Fun'
__date__ = '2018/2/4 16:55'

import traceback
import timeit
import inspect

TEST_NUM = 10000  # 单个测试用例的测试次数


class Test:
    def __init__(self, solution):
        self.solution = solution  # 解题实例
        self.pass_num = 0  # 通过测试的数量
        self.time_pool = []  # 耗时
        self.methods = list(filter(inspect.ismethod, (getattr(solution, name) for name in dir(solution))))  # 解题方法列表

    def print_runtime(self, time):
        if time < 1000:
            print('Average Runtime：{:.2f}μs\n'.format(time))
        elif time < 1000000:
            print('Average Runtime：{:.2f}ms\n'.format(time / 1000))
        else:
            print('Average Runtime：{:.2f}s\n'.format(time / 1000000))

    def test(self, testName, methodType, expected, *func_arg):
        # methodType表示要测试的方法，
        if testName is not None:
            print('{} begins:'.format(testName))

        try:
            start = timeit.default_timer()
            for i in range(TEST_NUM):
                self.methods[int(methodType) - 1](*func_arg)
            end = timeit.default_timer()
            result = self.convert(self.methods[int(methodType) - 1](*func_arg), *func_arg)
        except Exception as e:
            print('Failed: Syntax Error！')
            print(traceback.format_exc())
            return
        if (result == expected):
            average_runtime = ((end - start) / TEST_NUM) * 1000000
            print('Passed.')
            self.print_runtime(average_runtime)
            self.pass_num += 1
            self.time_pool.append(average_runtime)
        else:
            print('Failed: The test does not pass！')
            print('Expected: {}\nYour result: {}\n'.format(expected, result))

    def start_test(self):
        runtime = {}  # 各解题思路的耗时
        for method, method_name in enumerate(self.methods):
            self.pass_num = 0
            self.time_pool = []
            testArgs = self.my_test_code()
            test_num = len(testArgs)  # 总的测试数量
            i = 1
            for testArg in testArgs:
                testName = "Test" + str(method + 1) + "_" + str(i)
                self.test(testName, method + 1, testArg[-1], *tuple(testArg[:-1]))
                i += 1
            print('Result of Testing {}: {} / {}, {:.2f}%'.format(method_name.__name__,
                                                                  self.pass_num, test_num,
                                                                  (self.pass_num / test_num) * 100))
            if self.pass_num:
                time = sum(self.time_pool) / self.pass_num
                print('Total ', end='')
                self.print_runtime(time)
                runtime[method_name.__name__] = round(time, 2)
            print('*' * 100)
        print('Runtime Ranking（unit：μs）：\n{}'.format(sorted(runtime.items(), key=lambda x: x[1])))

    def my_test_code(self):
        # 只需在此处填写测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        testArgs = []
        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result
