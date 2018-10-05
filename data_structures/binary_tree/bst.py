__author__ = 'Hk4Fun'
__date__ = '2018/9/28 16:20'

from binary_tree import BinaryTree, TreeNode
from exceptions import InitError


class BST(BinaryTree):
    def __init__(self, root=None, serialize=None):
        super().__init__(root, serialize)
        if self._root and not self.is_bst():
            raise InitError("must start with a bst")

    def __contains__(self, val):
        cur = self.root
        while cur:
            if val < cur.val:
                cur = cur.left
            elif val > cur.val:
                cur = cur.right
            else:
                return True
        return False

    # 向二分搜索树中添加新的元素val
    def add(self, val):
        self._root = self._add(self.root, val)

    # 向以node为根的二分搜索树中插入元素val，递归算法
    # 返回插入新节点后二分搜索树的根
    def _add(self, node, val):
        if node is None:
            self._size += 1
            return TreeNode(val)
        if val < node.val:
            node.left = self._add(node.left, val)
        elif val > node.val:
            node.right = self._add(node.right, val)
        return node

    def minimum(self):
        return self._minimum(self.root).val if self.root else None

    # 寻找以node为根二分搜索树的最小元素结点，空树返回None
    def _minimum(self, node) -> TreeNode:
        if node:
            while node.left:
                node = node.left
            return node

    def maximum(self):
        return self._maximum(self.root).val if self.root else None

    # 寻找以node为根二分搜索树的最大元素结点，空树返回None
    def _maximum(self, node) -> TreeNode:
        if node:
            while node.right:
                node = node.right
            return node

    # 删除并返回二分搜索树的最小元素，空树返回None
    def remove_min(self):
        if self.root is None: return
        ret = self.minimum()
        self._root = self._remove_min(self.root)
        return ret

    # 删除掉以node为根的二分搜索树中的最小节点
    # 返回删除节点后新的二分搜索树的根
    def _remove_min(self, node) -> TreeNode:
        if node.left:  # 一直往左找
            node.left = self._remove_min(node.left)
            return node
        else:  # base case，来到最左端，返回右结点，相当于删掉当前结点（最左结点）
            self._size -= 1
            return node.right

    # 删除并返回二分搜索树的最大元素，空树返回None
    def remove_max(self):
        if self.root is None: return
        ret = self.maximum()
        self._root = self._remove_max(self.root)
        return ret

    def _remove_max(self, node) -> TreeNode:
        if node.right:
            node.right = self._remove_max(node.right)
            return node
        else:
            self._size -= 1
            return node.left

    def remove(self, val):
        self._root = self._remove(self.root, val)

    # 删除掉以node为根的二分搜索树中值为e的节点, 不存在就抛出ValueError，递归算法
    # 返回删除节点后新的二分搜索树的根
    def _remove(self, node, val) -> TreeNode:
        if node is None:
            raise ValueError('{!r} is not in BST')
        if val > node.val:  # 到右子树中删除
            node.right = self._remove(node.right, val)
            return node
        if val < node.val:  # 到左子树中删除
            node.left = self._remove(node.left, val)
            return node
        # 找到该结点，删除之
        if node.left is None:  # 左子树为空，返回右子树
            self._size -= 1
            return node.right
        if node.right is None:  # 右子树为空，返回左子树
            self._size -= 1
            return node.left
        # 既有左子树又有右子树，需要找到前驱结点或后继结点来代替当前结点
        next_node = self._next(node)  # 这里选择使用后继结点来代替当前结点
        next_node.right = self._remove_min(node.right)  # 后继结点的右子树为当前结点删除该后继结点的右子树
        next_node.left = node.left  # 后继结点的左子树为当前结点的左子树
        return next_node  # 返回的是该后继结点

    def _next(self, node) -> TreeNode:  # 后继结点为node右子树的最小结点
        return self._minimum(node.right) if node else None

    def _previous(self, node) -> TreeNode:  # 前驱结点为node左子树的最大结点
        return self._maximum(node.left) if node else None

    def add_values(self, values):
        for val in values:
            self.add(val)
