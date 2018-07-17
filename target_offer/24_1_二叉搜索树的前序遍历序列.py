__author__ = 'Hk4Fun'
__date__ = '2018/2/2 15:03'

'''题目描述：
输入一个整数数组，判断该数组是不是某二叉搜索树的前序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''
'''主要思路：
二叉搜索树对于每一个非叶子节点, 均有结点左子节点<当前节点<结点右子节点
前序序列的第一个值为二叉搜索树根节点的值，后面含有左子树和右子树结点
根据二叉搜索树的特性，根节点后面的序列分为两个区域，左边为左子树区，
值都比根节点小，右边为右子树区，值都比根节点大，
不满足该特性的序列就不是某二叉搜索树的前序遍历的结果，
注意左子树区域和右子树区域分别又是一棵二叉搜索树，因此递归检查这两个区域
题外话：通过题6和本题可知，树如果是二叉搜索树则可以只凭借前序或后序序列确定，
        否则还得再加上一个中序序列
'''


class Solution:
    def VerifySquenceOfBST1(self, pre_sequence):
        if not pre_sequence:
            return False

        root = pre_sequence[0]  # 取出根节点
        length = len(pre_sequence)

        i = 1
        # 在二叉搜索树中左子树结点小于根节点
        # i在循环结束后指向左子树区域右边界元素的右边那个元素（可能会越界，但不必担心）
        while i < length:
            if pre_sequence[i] > root:
                break
            i += 1

        # 在二叉搜索树中右子树结点大于根结点
        for j in range(i, length):
            if pre_sequence[j] < root:
                return False

        # 判断左子树是不是二叉搜索树
        left = True
        if i > 1:
            left = self.VerifySquenceOfBST1(pre_sequence[1:i])

        # 判断右子树是不是二叉搜索树
        right = True
        if i < length:
            right = self.VerifySquenceOfBST1(pre_sequence[i:])

        return left and right

    def VerifySquenceOfBST2(self, pre_sequence):
        # 简化版
        def verify(seq):
            if not seq or len(seq) == 1: return True
            root = seq[0]
            for i in range(1, len(seq)): # i会成为函数局部变量
                if seq[i] > root: break
            i += 1 # 进入右子树区域
            for j in range(i, len(seq)):
                if seq[j] < root: return False
            return verify(seq[1:i]) and verify(seq[i:])

        if not pre_sequence: return False
        return verify(pre_sequence)

# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        testArgs = []
        self.debug = True

        testArgs.append([[10, 6, 4, 8, 14, 12, 16], True])
        testArgs.append([[5, 4, 7, 6], True])
        testArgs.append([[5, 4, 3, 2, 1], True])
        testArgs.append([[1, 2, 3, 4, 5], True])
        testArgs.append([[5], True])
        testArgs.append([[7, 4, 6, 5], True])
        testArgs.append([[4, 6, 12, 8, 16, 14, 10], False])
        testArgs.append([[8, 6, 7, 5], False])
        testArgs.append([[], False])

        return testArgs


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
