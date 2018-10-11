__author__ = 'Hk4Fun'
__date__ = '2018/9/28 17:10'

from exceptions import DeserializeError, EmptyError


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({!r})'.format(self.val)


class BinaryTree:
    def __init__(self, root=None, serialize=None):
        self._root = root
        self._size = 0
        self._levels = 0
        if root:
            self._size = len(self.pre_order())
        elif serialize:
            if not isinstance(serialize, str):
                raise TypeError('serialize must be str')
            self._root = self.deserialize(serialize)

    def __repr__(self):
        return "{}(serialize='{}')".format(type(self).__name__, self.serialize())

    def __str__(self):
        treeList = self._level_order_with_None()
        levels = len(treeList)
        start = [(2 ** i - 1) for i in range(levels, 0, -1)]
        middle = [start[-1]] + start[:-1]
        s = []
        for i in range(levels):
            s.append(' ' * start[i])
            for v in treeList[i]:
                if v is None:
                    s.append(' ' * (middle[i] + 1))
                else:
                    s.append(str(v) + ' ' * middle[i])
            s.append('\n')
        return ''.join(s)

    def __eq__(self, other):
        if not isinstance(other, BinaryTree): return False
        return self._equal(self._root, other._root)

    @property
    def size(self):
        return self._size

    @property
    def leaf_nums(self):
        return self._leaf_count()

    @property
    def root(self):
        return self._root

    @property
    def levels(self):
        return self._depths(self.root)

    def _depths(self, node):
        if node is None: return 0
        return max(self._depths(node.left), self._depths(node.right)) + 1

    def is_empty(self):
        return self.size == 0

    def pre_order(self):
        return self._traverse('pre')

    def in_order(self):
        return self._traverse('in')

    def post_order(self):
        return self._traverse('post')

    def level_order(self):
        if self.root is None: return []
        res, level = [], [self.root]
        while level:
            next_level = []
            res.append([])
            for node in level:
                res[-1].append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level
        return res

    def serialize(self):
        levels = self._level_order_with_None()
        return ','.join(str(val) if val else '#' for level in levels for val in level)

    def deserialize(self, s):
        s = s.split(',')
        if not (len(s) & 1):
            raise DeserializeError('deserialize failed when building a binary tree')
        if s[0] == '#': return
        root = TreeNode(int(s[0]))
        queue = [root]
        self._size += 1
        for i in range(1, len(s), 2):  # s的长度一定为奇数
            node = queue.pop(0)  # 待连接的结点
            if node:
                if s[i] != '#':  # 连接左孩子
                    left = TreeNode(int(s[i]))
                    self._size += 1
                else:
                    left = None
                queue.append(left)
                node.left = left

                if s[i + 1] != '#':  # 连接右孩子
                    right = TreeNode(int(s[i + 1]))
                    self._size += 1
                else:
                    right = None
                queue.append(right)
                node.right = right
        return root

    def _equal(self, root1, root2):
        if root1 and root2 and root1.val == root2.val:
            return self._equal(root1.left, root2.left) and self._equal(root1.right, root2.right)
        return not root1 and not root2

    def _level_order_with_None(self):
        level, res = [self.root], []
        while any(level):
            res.append([])
            next_level = []
            for cur in level:
                if cur:
                    res[-1].append(cur.val)
                    next_level += (cur.left, cur.right)
                else:
                    res[-1].append(None)
                    next_level += (None, None)
            level = next_level
        return res

    def _traverse(self, order='pre'):
        if not self.root: return []
        stack, res = [(self.root, False)], []
        while stack:
            cur, visited = stack.pop()
            if not cur:
                continue
            if visited:
                res.append(cur.val)
            else:
                if order == 'post':
                    stack.append((cur, True))
                stack.append((cur.right, False))
                if order == 'in':
                    stack.append((cur, True))
                stack.append((cur.left, False))
                if order == 'pre':
                    stack.append((cur, True))
        return res

    def is_bst(self):
        return self._is_bst(self.root, -float('inf'), float('inf'))

    def _is_bst(self, node, min_val, max_val):
        if node is None: return True
        return (
                min_val < node.val < max_val and
                self._is_bst(node.left, min_val, node.val) and
                self._is_bst(node.right, node.val, max_val)
        )

    def is_full(self):
        return self.size == 2 ** self.levels - 1

    def is_complete(self):
        if self.root is None: return True
        queue = [self.root]
        appear_none = False
        while queue:
            node = queue.pop(0)
            if node is None:
                if not appear_none:  # 首次出现空结点
                    appear_none = True
            else:
                if not appear_none:  # 还未出现空结点
                    queue.append(node.left)
                    queue.append(node.right)
                else:  # 之前出现过空结点
                    return False
        return True

    def _leaf_count(self):
        # 从结点数上看：n0 + n1 + n2 = S
        # 从树枝数上看：0*n0 + 1*n1 + 2*n2 = S-1
        # 所以：n0 = n2 + 1......@1
        # 即：二叉树的叶子结点数总是比度为2的结点数多1
        # 对于满二叉树来讲，没有度为1的结点
        # 所以：n0 + n2 = S......@2
        # 由@1和@2，得：n0 = (S+1)/2
        # 又因为：S = 2 ** levels - 1
        # 所以，对于满二叉树来讲：n0 = 2 ** (levels - 1)
        if self.root is None: return 0
        stack = [self.root]  # 非递归前序遍历
        nums = 0
        while stack:
            node = stack.pop()
            if node.left is None and node.right is None:
                nums += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return nums

    def is_strict(self):
        # 非叶子结点都是度为2的结点为严格二叉树
        # 也就是说没有度为1的结点
        # 由 _leaf_count 注释可知，当 n1=0 时，n0=(S+1)/2
        # 所以只需证明当 n0=(S+1)/2 时，n1=0即可
        # 因为：n0 = n2 + 1 且 n0 + n1 + n2 = S
        # 所以：2*n0 + n1 = S + 1，将 n0=(S+1)/2 带入
        # 得：n1 = 0
        # 所以只需判断 n0 是否等于 (S+1)/2 即可
        if self.is_full(): return True  # 满二叉树为严格二叉树
        return self.leaf_nums == (self.size + 1) / 2  # 这里不能'//'

    def is_balanced(self):
        return self._is_balanced(self.root) >= 0

    def _is_balanced(self, node):
        if node is None: return 0
        left = self._is_balanced(node.left)
        if left < 0: return -1
        right = self._is_balanced(node.right)
        if right < 0: return -1
        return -1 if abs(left - right) > 1 else max(left, right) + 1

    def max_distance(self):
        if self.root is None:
            raise EmptyError('empty tree has no distance')
        return self._depths(self.root.left) + self._depths(self.root.right)
