__author__ = 'Hk4Fun'
__date__ = '2018/2/20 22:05'

'''题目描述：
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1]
使得B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]，不能使用除法。
'''
'''主要思路：
思路1（时间O(n^2)，空间O(1)）：暴力法
思路2（时间O(n)，空间O(n)）：把B[i]拆成前i项和后（n-i）项，分别求乘积，再相乘
                            即B[i]=C[i]*D[i]=(A[0]*A[1]*...*A[i-1])*(A[i+1]*...*A[n-1])
                            而C[i]=C[i-1]*A[i-1], D[i]=A[i+1]*D[i+1]
思路3（时间O(n)，空间O(1)）：思路2的优化，利用数组B的空间来节省数组C和D的空间
'''


class Solution:
    def multiply1(self, A):
        if not A or len(A) == 1:
            return
        length = len(A)
        B = []
        for i in range(length):
            mul = 1
            for j in range(length):
                if i != j:
                    mul *= A[j]
            B.append(mul)
        return B

    def multiply2(self, A):
        if not A or len(A) == 1:
            return
        length = len(A)
        B = []
        forward = [1]
        backward = [1]
        for i in range(1, length):
            forward.append(A[i - 1] * forward[i - 1])  # 自上而下计算上三角
            backward.append(A[length - i] * backward[i - 1])  # 自下而上计算下三角
        for i in range(length):
            B.append(forward[i] * backward[length - i - 1])
        return B

    def multiply3(self, A):
        if not A: return
        B = [1]
        for i in range(1, len(A)):
            B.append(B[i - 1] * A[i - 1])  # 自上而下计算上三角
        tmp = 1 # 关键之处，D[i]只与D[i+1]有关，因此可以节约空间为O(1)
        for i in range(len(A) - 2, -1, -1):
            tmp *= A[i + 1]  # 自下而上计算下三角
            B[i] *= tmp  # B[i]=C[i]*D[i]
        return B


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        self.debug = True
        testArgs = []

        testArgs.append([[1, 2, 3, 4, 5], [120, 60, 40, 30, 24]])
        testArgs.append([[1, 2, 0, 4, 5], [0, 0, 40, 0, 0]])
        testArgs.append([[1, 2, 0, 4, 0], [0, 0, 0, 0, 0]])
        testArgs.append([[1, -2, 3, -4, 5], [120, -60, 40, -30, 24]])
        testArgs.append([[1, -2], [-2, 1]])
        testArgs.append([[1], None])
        testArgs.append([[], None])
        testArgs.append([None, None])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
