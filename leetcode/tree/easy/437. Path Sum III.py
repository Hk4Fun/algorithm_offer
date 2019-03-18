__author__ = 'Hk4Fun'
__date__ = '2018/4/21 19:46'
'''题目描述：
You are given a binary tree in which each node contains an integer value.
Find the number of paths that sum to a given value.
The path does not need to start or end at the root or a leaf, 
but it must go downwards (traveling only from parent nodes to child nodes).
The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''
'''主要思路：
思路1（时间O（nlogn），空间O（n））
暴力dfs

思路2（时间O（n），空间O（n））
哈希表记录根节点到每一结点的和，值为和出现的次数

'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    :type root: TreeNode
    :type sum: int
    :rtype: int
    """

    def pathSum1(self, root, sum):
        def path(root, sum):
            if not root: return 0
            return path(root.left, sum - root.val) + path(root.right, sum - root.val) + int(root.val == sum)

        if not root: return 0
        return path(root, sum) + self.pathSum1(root.left, sum) + self.pathSum1(root.right, sum)

    def pathSum2(self, root, sum):
        def findPaths(root, cur_sum):
            if not root: return
            cur_sum += root.val
            if cur_sum - sum in self.cache:  # cur_sum - self.target就是(root-->start)
                self.count += self.cache[cur_sum - sum]
            self.cache[cur_sum] = self.cache.setdefault(cur_sum, 0) + 1
            findPaths(root.left, cur_sum)
            findPaths(root.right, cur_sum)
            self.cache[cur_sum] -= 1  # 记得减回去，因为其他节点不再以该结点为祖先

        self.count = 0
        self.cache = {0: 1}  # 保证从根节点出发的和被统计
        findPaths(root, 0)
        return self.count


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])

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
