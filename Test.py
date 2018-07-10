__author__ = 'Hk4Fun'
__date__ = '2018/2/4 16:55'

import traceback
import timeit
import inspect
import copy


class Test:
    def __init__(self, solution):
        self.solution = solution  # 解题实例
        self.pass_num = 0  # 通过测试的数量
        self.time_pool = []  # 耗时
        self.debug = False  # debug模式下每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 10000  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        self.methods = list(filter(inspect.ismethod, (getattr(solution, name) for name in dir(solution))))  # 解题方法列表

    def print_runtime(self, time):  # time单位：μs
        if time < 1000:
            print('Average Runtime：{:.2f}μs\n'.format(time))
        elif time < 1000000:
            print('Average Runtime：{:.2f}ms\n'.format(time / 1000))
        else:
            print('Average Runtime：{:.2f}s\n'.format(time / 1000000))

    def test(self, method_num, expected, *func_arg):
        # method_num 表示要测试的解题方法序号
        try:
            total_time = 0
            for i in range(1 if self.debug else self.TEST_NUM):
                func_arg_copy = copy.deepcopy(func_arg)  # 防止func_arg被原地修改
                start = timeit.default_timer()
                self.methods[int(method_num) - 1](*func_arg_copy)
                end = timeit.default_timer()
                total_time += end - start
            func_arg_copy = copy.deepcopy(func_arg)
            result = self.convert(self.methods[int(method_num) - 1](*func_arg_copy), *func_arg_copy)
        except Exception:
            print('Failed: Syntax Error！')
            print(traceback.format_exc())
            return

        if self.checked(result, expected, *func_arg):
            average_runtime = (total_time / (1 if self.debug else self.TEST_NUM)) * 1000000
            print('Passed.')
            self.print_runtime(average_runtime)
            self.pass_num += 1
            self.time_pool.append(average_runtime)
        else:
            print('Failed: The test does not pass！')
            print('Test for: {}'.format(func_arg))
            print('Your result: {}\nBut expected: {}\n'.format(result, expected))

    def start_test(self):
        begin = timeit.default_timer()
        runtime = {}  # 各解题思路的耗时
        testArgs = self.my_test_code()
        test_num = len(testArgs)  # 总的测试数量
        for i, method in enumerate(self.methods):
            self.pass_num = 0
            self.time_pool = []
            testArgs_copy = copy.deepcopy(testArgs)
            for j, testArg in enumerate(testArgs_copy):
                print('Test for {}_{}:'.format(method.__name__, j + 1))
                self.test(i + 1, testArg[-1], *tuple(testArg[:-1]))
            fmt = 'Result of Testing {}: {} / {}, {:.2f}%'
            print(fmt.format(method.__name__, self.pass_num, test_num, (self.pass_num / test_num) * 100))
            if self.pass_num:
                time = sum(self.time_pool) / self.pass_num
                print('Total ', end='')
                self.print_runtime(time)
                if self.pass_num == test_num:  # 通过全部测试才加入排行版进行排名
                    runtime[method.__name__] = round(time, 2)
            print('*' * 100)
        end = timeit.default_timer()
        template = 'Test Result (unit：μs, test_num: {}*{}, test_time:{:.4f} s)：'
        print(template.format(test_num, 1 if self.debug else self.TEST_NUM, end - begin))
        for i, v in enumerate(sorted(runtime.items(), key=lambda x: x[1]), 1):
            print('{:2}、{:20}: {}'.format(i, v[0], v[1]))

    def my_test_code(self):
        # 只需在此处填写测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        testArgs = []
        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected
