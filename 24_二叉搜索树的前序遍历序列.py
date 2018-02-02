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
    def VerifySquenceOfBST(self, pre_sequence):
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
            left = self.VerifySquenceOfBST(pre_sequence[1:i])

        # 判断右子树是不是二叉搜索树
        right = True
        if i < length:
            right = self.VerifySquenceOfBST(pre_sequence[i:])

        return left and right


# ================================测试代码================================
import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 总的测试数量
time_pool = []  # 耗时


def Test(testName, pre_sequence, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    test = Solution()
    try:
        start = timeit.default_timer()
        result = test.VerifySquenceOfBST(pre_sequence)
        end = timeit.default_timer()

    except Exception as e:
        print('Failed:语法错误！')
        print(traceback.format_exc())
        return
    if (result == expected):
        print('Passed.\n')
        pass_num += 1
        time_pool.append(end - start)
    else:
        print('Failed:测试不通过！\n')


Test('Tset1', [10, 6, 4, 8, 14, 12, 16], True)
Test('Tset2', [5, 4, 7, 6], True)
Test('Tset3', [5, 4, 3, 2, 1], True)
Test('Tset4', [1, 2, 3, 4, 5], True)
Test('Tset5', [5], True)
Test('Tset6', [7, 4, 6, 5], True)
Test('Tset7', [4, 6, 12, 8, 16, 14, 10], False)
Test('Tset8', [8, 6, 7, 5], False)
Test('Tset9', [], False)

print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))
