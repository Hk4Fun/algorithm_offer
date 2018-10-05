__author__ = 'Hk4Fun'
__date__ = '2018/10/5 16:28'

from bst import BST, TreeNode as Node
from exceptions import InitError


class TreeNode(Node):
    def __init__(self, val=None, left=None, right=None):
        super().__init__(val, left, right)
        self.height = 1


class AVLTree(BST):
    def __init__(self, root=None, serialize=None):
        super().__init__(root, serialize)
        if self._root and not self.is_balanced():
            raise InitError("must start with a AVLTree")

    def _get_height(self, node):
        if node is None: return 0
        return node.height

    def _get_balance_factor(self, node):
        if node is None: return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _add(self, node, val):
        if node is None:
            self._size += 1
            return TreeNode(val)
        if val < node.val:
            node.left = self._add(node.left, val)
        elif val > node.val:
            node.right = self._add(node.right, val)

        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1
        return self._keep_balance(node)

    def _remove_min(self, node):
        if node.left:  # 一直往左找
            node.left = self._remove_min(node.left)
            retNode = node
        else:  # base case，来到最左端，返回右结点，相当于删掉当前结点（最左结点）
            self._size -= 1
            retNode = node.right
        if retNode is None: return
        retNode.height = max(self._get_height(retNode.left), self._get_height(retNode.right)) + 1
        return self._keep_balance(retNode)

    def _remove_max(self, node):
        if node.right:
            node.right = self._remove_max(node.right)
            retNode = node
        else:
            self._size -= 1
            retNode = node.right
        if retNode is None: return
        retNode.height = max(self._get_height(retNode.left), self._get_height(retNode.right)) + 1

        return self._keep_balance(retNode)

    def _remove(self, node, val):
        if node is None:
            raise ValueError('{!r} is not in BST')
        if val > node.val:  # 到右子树中删除
            node.right = self._remove(node.right, val)
            retNode = node
        elif val < node.val:  # 到左子树中删除
            node.left = self._remove(node.left, val)
            retNode = node
        else:  # 找到该结点，删除之
            if node.left is None:  # 左子树为空，返回右子树
                self._size -= 1
                retNode = node.right
            elif node.right is None:  # 右子树为空，返回左子树
                self._size -= 1
                retNode = node.left
            else:  # 既有左子树又有右子树，需要找到前驱结点或后继结点来代替当前结点
                retNode = self._next(node)  # 这里选择使用后继结点来代替当前结点
                retNode.right = self._remove_min(node.right)  # 后继结点的右子树为当前结点删除该后继结点的右子树
                retNode.left = node.left  # 后继结点的左子树为当前结点的左子树
        if retNode is None: return
        retNode.height = max(self._get_height(retNode.left), self._get_height(retNode.right)) + 1
        return self._keep_balance(retNode)

    def _keep_balance(self, node):
        balance_factor = self._get_balance_factor(node)
        if balance_factor > 1 and self._get_balance_factor(node.left) >= 0:  # LL
            return self._right_rotate(node)
        if balance_factor < -1 and self._get_balance_factor(node.right) <= 0:  # RR
            return self._left_rotate(node)
        if balance_factor > 1 and self._get_balance_factor(node.left) < 0:  # LR
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance_factor < -1 and self._get_balance_factor(node.right) > 0:  # RL
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        return node  # 已经保持平衡，直接返回

    def _left_rotate(self, y):
        """对节点y进行向左旋转操作，返回旋转后新的根节点x
               y                             x
             /  \                          /   \
            T1   x      向左旋转 (y)       y     z
                / \   - - - - - - - ->   / \   / \
              T2  z                     T1 T2 T3 T4
                 / \
                T3 T4
        """
        x = y.right
        T2 = x.left
        x.left = y
        y.right = T2
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        return x

    def _right_rotate(self, y):
        """
        对节点y进行向右旋转操作，返回旋转后新的根节点x
                y                              x
               / \                           /   \
              x   T4     向右旋转 (y)        z     y
             / \       - - - - - - - ->    / \   / \
            z   T3                       T1  T2 T3 T4
           / \
         T1   T2
        """
        x = y.left
        T3 = x.right
        x.right = y
        y.left = T3
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        return x
