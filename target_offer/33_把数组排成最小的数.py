__author__ = 'Hk4Fun'
__date__ = '2018/2/10 20:22'

'''题目描述：
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''
'''主要思路：
最直接的做法就是把数组中所有数字进行全排列，然后把每个排列拼接起来，最后求出拼起来的数字的最小值，
易知算法复杂度高达O(n!)，所以不推荐。这里定义一个新的比较规则：
对于两个数字m,n，可以拼接成mn和nm。若mn<nm，则定义m<n；若mn>nm，则定义m>n；若mn=nm，则定义m=n
将数组中的数按照上述比较规则从小到大进行排序，最后将排序的数组进行拼接即为数组所能拼成的最小数
证明见书第一版P179~180
'''
from functools import cmp_to_key

# cmp_to_key 的实现原理很有意思。。。
# 其返回一个实现了各种比较方法的类：class K
# 当key做映射时，会把K当作函数调用，K(obj)
# 这样实际上是创建（返回）了一个K的实例（实在是妙啊！）
# 也就相当于把参与比较的元素映射成了一个K的实例
# 来看构造函数就明白了：
# def __init__(self, obj):
#     self.obj = obj
# 就是把obj保存起来了而已
# 关键看其中实现的各种比较方法，比如：
# def __lt__(self, other):
#     return mycmp(self.obj, other.obj) < 0
# 在遇到两两比较时，比如"<"，就会触发该方法，然后把另一个obj当作other传进来比较
# 怎么比较？mycmp就是cmp_to_key(mycmp)的参数，就是自己定义的含有两个参数的lambda！
# 所以我们梳理一下cmp_to_key是如何把含有两个参数的lambda转换成只含有一个参数的lambda的：
# 传入的含有两个参数的lambda被当作比较函数，在后面遇到两两比较时被触发调用，
# 而转换成只含有一个参数的lambda实际上是转换成一个构造函数为只含有一个参数的类K，
# 只不过其调用方式刚好和只含有一个参数的lambda一致，让人以为真的转换成只含有一个参数的lambda
# 所以key返回的对象必须是可比较对象，不管是lambda实现还是类实现
# py3为什么要去掉cmp而只保留key，因为key比cmp更高效：
# 在每一个元素上，key只会被调用1次，而cmp这个双参数比较函数则会在每一次两两比较时被调用

class Solution:
    def PrintMinNumber(self, numbers):
        if numbers:
            return ''.join(sorted([str(i) for i in numbers], key=cmp_to_key(lambda x, y: int(x + y) - int(y + x))))


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        testArgs.append([[3, 5, 1, 4, 2], '12345'])

        testArgs.append([[3, 32, 321], '321323'])

        testArgs.append([[3, 323, 32123], '321233233'])

        testArgs.append([[1, 11, 111], '111111'])

        testArgs.append([[321], '321'])

        testArgs.append([[], None])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
