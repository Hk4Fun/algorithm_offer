__author__ = 'Hk4Fun'
__date__ = '2018/3/13 11:38'
'''题目来源:
爱奇艺2018秋季校招C++工程师(第三场)编程题第三题
'''
'''题目描述：
牛牛选择了一个正整数X，然后把它写在黑板上。然后每一天他会擦掉当前数字的最后一位，
知道他擦掉所有的数位。在整个过程中，牛牛会把所有在黑板上出现过的数字记录下来，然后求出他们的总和sum.
例如X=509，在黑板上出现过的数字一次是509,50,5，他们的和就是564.
牛牛现在给出一个sum，牛牛想让你求出一个正整数X经过上述过程的结果是sum，
1<=sum<=10^18.没有这样的X就输出-1.
'''
'''主要思路：
思路1（时间O（lgn*logn），空间O（1））：
二分法。sum(x)=x+x//10+x//100+......,该函数单调递增，故用二分法找到x，正向运算
其中上界为sum，下界为0

思路2（时间O（lgn），空间O（1））：
假设x=abc=100a+10b+c，则ab=10a+b，a=a，上述三个式子加起来：sum=abc+ab+a=111a+11b+c
所以逆向运算有：
a=sum//111 (因为11b+c<111), b=(sum-111a)//11(因为c<11), c=(sum-111a-11b)//1
最终x=abc=100a+10b+c
当然，若算出来的a、b、c大于9就不存在这样的x了
'''


class Solution:
    def method1(self, sum):
        if sum == None or sum < 0:
            return -1
        if sum < 10:
            return sum
        l, r = 0, sum
        while l <= r:
            mid = l + ((r - l) >> 1)
            tmp, n = 0, mid
            while n:
                tmp += n
                n //= 10
            if tmp == sum:
                return mid
            elif tmp > sum:
                r = mid - 1
            else:
                l = mid + 1
        return -1

    def method2(self, sum):
        if sum == None or sum < 0:
            return -1
        if sum < 10:
            return sum
        n = len(str(sum))
        res = 0
        divisor = (10 ** n - 1) // 9
        for i in range(n):
            x = sum // divisor
            if x > 9: break
            sum -= x * divisor
            res = res * 10 + x
            divisor = divisor // 10
        return res if not sum else -1


# ================================测试代码===============================

from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = True  # debug模式下每个测试用例只测试一遍，默认情况下关闭debug模式
        testArgs = []

        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        def Sum(n):
            sum = 0
            while n:
                sum += n
                n //= 10
            return sum

        testArgs.append([Sum(0), 0])
        testArgs.append([Sum(1), 1])
        testArgs.append([Sum(2), 2])
        testArgs.append([Sum(10), 10])
        testArgs.append([Sum(20), 20])
        testArgs.append([Sum(1234), 1234])
        testArgs.append([87, -1])
        testArgs.append([98, -1])
        testArgs.append([1097, -1])
        testArgs.append([-1, -1])
        testArgs.append([None, -1])

        # 批量测试
        for i in range(10 **5):
            testArgs.append([Sum(i), i])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
