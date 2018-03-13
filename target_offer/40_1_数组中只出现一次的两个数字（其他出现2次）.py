__author__ = 'Hk4Fun'
__date__ = '2018/2/14 16:31'

'''题目描述：
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''
'''主要思路：
思路1（时间复杂度O(n)，空间复杂度O(1)）：
       既然其他的数字都出现了两次，那么可以把数组中所有数异或，则两次的相互抵消，一次的相互异或，
       即最终的异或结果相当于两个出现一次的数相异或。如果只有一个数字是出现一次的，那么异或结果
       就是那个数了，但这里有两个，于是我们想着把它俩给分开，使得各自在一个数组里，且每个数组除
       了那个出现一次的数以外其他数都是出现两次，这样两个数组分别异或就可以找出这两个数了。
       关键是如何把它俩分开且数组里其他数都是成双成对？我们仍然把整个数组相异或，得到的结果一定
       不为0（因为这两个数一定不一样），那么二进制中一定有一个位置为1。那么我们可以以最右边的1
       为标准，把整个数组中该位为1的数划分为一组，为0的划分为一组。这样做一举两得：一来把那两个
       出现一次的数分开了，二来把成对的数放在了同一个数组里了（因为相同的数其二进制位一致）。
思路2（时间复杂度O(n^2)，空间复杂度O(n)）：
       暴力枚举，遍历整个数组，同时用一个临时数组来存放之前出现过的数字。如果当前数字在临时数组中
       存在，则把该数字在临时数组中删除；如果不存在就直接放进临时数组中。这样最终的临时数组就
       只剩下只出现一次的数。
思路3：pythonic, 使用collections中的Counter，其时间复杂度和空间复杂度明显是比较大的，但可以看出：
       没有什么是python不能一行解决的，如果有就两行！
'''


class Solution:
    # 返回[a,b] 其中a，b是出现一次的两个数字
    def FindNumsAppearOnce1(self, array):
        if array and len(array) > 1:
            xor_sum = 0
            for i in array:
                xor_sum ^= i
            a = b = 0
            for i in array:
                # ~xor_sum + 1使最右边的1和后面的0不变，前面的位全部取反，
                # & xor_sum 后就把xor_sum最右边的1筛选出来，其他位为0
                if i & ((~xor_sum + 1) & xor_sum):
                    a ^= i
                else:
                    b ^= i
            return [a, b]

    def FindNumsAppearOnce2(self, array):
        if array and len(array) > 1:
            tmp = []
            for i in array:
                if i in tmp:
                    tmp.remove(i)
                else:
                    tmp.append(i)
            return tmp

    def FindNumsAppearOnce3(self, array):
        from collections import Counter
        return list(map(lambda c: c[0], Counter(array).most_common()[-2:])) if (array and len(array) > 1) else None


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        testArgs.append([[2, 4, 3, 6, 3, 2, 5, 5], {4, 6}])

        testArgs.append([[4, 6], {4, 6}])

        testArgs.append([[4, 6, 1, 1, 1, 1], {4, 6}])

        testArgs.append([[1], None])

        testArgs.append([[], None])

        return testArgs

    def convert(self, result, *func_arg):
        return set(result) if result else result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
