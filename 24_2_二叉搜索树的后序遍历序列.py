__author__ = 'Hk4Fun'
__date__ = '2018/2/1 18:04'

'''题目描述：
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''
'''主要思路：
二叉搜索树对于每一个非叶子节点, 均有结点左子节点<当前节点<结点右子节点
后序序列的最后一个值为二叉搜索树根节点的值，前面含有左子树和右子树结点
根据二叉搜索树的特性，根节点前面的序列分为两个区域，左边为左子树区，
值都比根节点小，右边为右子树区，值都比根节点大，
不满足该特性的序列就不是某二叉搜索树的后序遍历的结果，
注意左子树区域和右子树区域分别又是一棵二叉搜索树，因此递归检查这两个区域
'''


class Solution:
    def VerifySquenceOfBST(self, post_sequence):
        if not post_sequence:
            return False

        root = post_sequence[-1]  # 取出根节点
        length = len(post_sequence)

        i = 0
        # 在二叉搜索树中左子树结点小于根节点
        # 注意：这里不能用
        # for i in range(length - 1)：
        #     if post_sequence[i] > root:
        #         break
        # 因为我们要让i在循环结束后指向左子树区域右边界元素的右边那个元素
        # 体会一下test2和test7的特殊性就明白了
        while i < length - 1:
            if post_sequence[i] > root:
                break
            i += 1

        # 在二叉搜索树中右子树结点大于根结点
        for j in range(i, length - 1):
            if post_sequence[j] < root:
                return False

        # 判断左子树是不是二叉搜索树
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(post_sequence[:i])

        # 判断右子树是不是二叉搜索树
        right = True
        if i < length - 1:
            right = self.VerifySquenceOfBST(post_sequence[i:length - 1])

        return left and right


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        testArgs = []

        testArgs.append([[4, 8, 6, 12, 16, 14, 10], True])
        testArgs.append([[4, 6, 7, 5], True])
        testArgs.append([[1, 2, 3, 4, 5], True])
        testArgs.append([[5, 4, 3, 2, 1], True])
        testArgs.append([[5], True])
        testArgs.append([[7, 4, 6, 5], False])
        testArgs.append([[7, 5, 6, 8], False])
        testArgs.append([[4, 6, 12, 8, 16, 14, 10], False])
        testArgs.append([[], False])

        return testArgs


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()
