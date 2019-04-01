__author__ = 'Hk4Fun'
__date__ = '2019/4/1 10:35'


class Solution:
    def KMP(self, s, m):
        def get_next_arr(m):
            if len(m) == 1: return [-1]
            next_arr = [-1, 0]
            cn, pos = 0, 2
            while pos < len(m):
                if m[pos - 1] == m[cn]:
                    next_arr.append(cn + 1)
                    pos += 1
                    cn += 1
                elif cn > 0:
                    cn = next_arr[cn]
                else:
                    next_arr.append(0)
                    pos += 1
            return next_arr

        if not s or not m or len(s) < len(m): return -1
        next_arr = get_next_arr(m)
        si = mi = 0
        while si < len(s) and mi < len(m):
            if s[si] == m[mi]:
                si += 1
                mi += 1
            elif next_arr[mi] == -1:
                si += 1
            else:
                mi = next_arr[mi]
        return si - mi if mi == len(m) else -1


# ================================测试代码================================


from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = True  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 10  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []

        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        testArgs.append(['abcabcababaccc', 'ababa', 6])
        testArgs.append(['asda', 'w', -1])
        testArgs.append(['as', 'asas', -1])


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
