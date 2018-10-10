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
       不为0（因为这两个数一定不一样），那么二进制中一定有一个位置为1。于是我们可以以最右边的1
       为标准，把整个数组中该位为1的数划分为一组，为0的划分为一组。这样做一举两得：一来把那两个
       出现一次的数分开了，二来把成对的数放在了同一个数组里了（因为相同的数其二进制位一致）。
       其实还可以再优化一下：在第二次循环时，只需把标准位是1的数异或起来就可以了，
       那么最终结果就是那两个数字中的一个，此时把该数与第一次循环的异或结果再次异或就可以拿到另一个数了
思路2（时间复杂度O(n)，空间复杂度O(n)）：
       暴力枚举，遍历整个数组，同时用一个临时数组来存放之前出现过的数字。如果当前数字在临时数组中
       存在，则把该数字在临时数组中删除；如果不存在就直接放进临时数组中。这样最终的临时数组就
       只剩下只出现一次的数。

该题可以扩展为数组中有两个数出现了奇数次（次数不一定相等，也不一定为1），
其他数都出现了偶数次（次数不一定相等，也不一定为2），其解题思路没有任何改动
'''


class Solution:
    def FindNumsAppearOnce1(self, array):
        if array and len(array) > 1:
            xor_sum = a = 0
            for i in array:
                xor_sum ^= i
            last1 = (-xor_sum) & xor_sum  # 取出最右边的1
            for i in array:
                if i & last1:
                    a ^= i
            return [a, a ^ xor_sum]

    def FindNumsAppearOnce2(self, array):
        if array and len(array) > 1:
            res = set()
            for i in array:
                if i in res:
                    res.remove(i)
                else:
                    res.add(i)
            return res


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

        testArgs.append([[4, 4, 4, 6, 6, 6, 1, 1, 1, 1, 2, 2], {4, 6}])

        testArgs.append([[1], None])

        testArgs.append([[], None])

        return testArgs

    def convert(self, result, *func_arg):
        return set(result) if result else result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
