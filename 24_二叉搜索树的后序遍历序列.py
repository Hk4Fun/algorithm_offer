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
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False

        root = sequence[-1]  # 取出根节点
        length = len(sequence)

        i = 0
        # 在二叉搜索树中左子树结点小于根节点
        for i in range(length - 1):
            if sequence[i] > root:
                break

        # 在二叉搜索树中右子树结点大于根结点
        # 注意这里是 i + 1,而不是 i，因为当前面元素都小于根节点时，i指向倒数第二个元素
        # range(i + 1, length - 1)=range(length - 2, length - 1), 会进入该循环
        # 而此时sequence[j] = sequence[length - 2] < root,所以会False，而事实上为True
        # 根本原因就在于进入了该循环，j应该始终从比根节点大的元素开始索引
        for j in range(i + 1, length - 1):
            if sequence[j] < root:
                return False

        # 判断左子树是不是二叉搜索树
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])

        # 判断右子树是不是二叉搜索树
        right = True
        if i < length - 1:
            right = self.VerifySquenceOfBST(sequence[i:length - 1])

        return left and right


# ================================测试代码================================
import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 总的测试数量
time_pool = []  # 耗时


def Test(testName, sequence, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    test = Solution()
    try:
        start = timeit.default_timer()
        result = test.VerifySquenceOfBST(sequence)
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


Test('Tset1', [4, 8, 6, 12, 16, 14, 10], True)
Test('Tset2', [4, 6, 7, 5], True)
Test('Tset3', [1, 2, 3, 4, 5], True)
Test('Tset4', [5, 4, 3, 2, 1], True)
Test('Tset5', [5], True)
Test('Tset6', [7, 4, 6, 5], False)
Test('Tset7', [4, 6, 12, 8, 16, 14, 10], False)
Test('Tset8', [], False)

print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))
