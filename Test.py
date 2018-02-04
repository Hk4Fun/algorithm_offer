__author__ = 'Hk4Fun'
__date__ = '2018/2/4 16:55'

# ================================测试代码================================
import traceback
import timeit
import inspect

class Test:
    def __init__(self, Solution, methodNum):
        self.Solution = Solution  # 被测试函数所在的类
        self.methodNum = methodNum # 测试的方法数
        self.pass_num = 0  # 通过测试的数量
        self.time_pool = []  # 耗时

    def test(self, testName, methodType, expected, *func_arg):
        # methodType表示要测试的方法，
        if testName is not None:
            print('{} begins:'.format(testName))
        solution= self.Solution()
        attrs = (getattr(solution, name) for name in dir(solution))
        methods = list(filter(inspect.ismethod, attrs))
        try:
            start = timeit.default_timer()
            result = methods[int(methodType)-1](*func_arg)
            end = timeit.default_timer()
        except Exception as e:
            print('Failed:语法错误！')
            print(traceback.format_exc())
            return
        if (result == expected):
            print('Passed.\n')
            self.pass_num += 1
            self.time_pool.append(end - start)
        else:
            print('Failed:测试不通过！\n')

    def start_test(self, testArgs):
        test_num = len(testArgs)  # 总的测试数量
        for method in range(1, self.methodNum + 1):
            self.pass_num = 0
            self.time_pool = []
            i = 1
            for testArg in testArgs:
                testName = "Test" + str(method) + "_" + str(i)
                self.test(testName, method, testArg[-1], *tuple(testArg[:-1]))
                i += 1
            print('测试结果：{}/{},{:.2f}%'.format(self.pass_num, test_num, (self.pass_num / test_num) * 100))
            if self.pass_num:
                print('平均耗时：{:.2f}μs\n'.format((sum(self.time_pool) / self.pass_num) * 1000000))

    def my_test_code(self):
        # 在此处填写测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        pass
