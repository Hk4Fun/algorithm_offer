__author__ = 'Hk4Fun'
__date__ = '2018/10/28 20:38'

from bst import BinaryTree


def pre_order1(root):
    if root is None: return []
    stack, res = [root], []
    while stack:
        cur = stack.pop()
        res.append(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return res


def pre_order2(root):
    if root is None: return []
    stack, res = [], []
    cur = root
    while stack or cur:
        while cur:
            res.append(cur.val)
            stack.append(cur)
            cur = cur.left
        cur = stack.pop().right
    return res


def pre_order3(root):
    if root is None: return []
    stack, res = [], []
    cur = root
    while stack or cur:
        if cur:
            res.append(cur.val)
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop().right
    return res


def pre_order4(root):
    if root is None: return []
    stack, res = [(root, False)], []
    while stack:
        cur, visited = stack.pop()
        if cur is None: continue
        if visited:
            res.append(cur.val)
        else:
            stack.append((cur.right, False))
            stack.append((cur.left, False))
            stack.append((cur, True))
    return res


def in_order1(root):
    if root is None: return []
    stack, res = [], []
    cur = root
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res


def in_order2(root):
    if root is None: return []
    stack, res = [], []
    cur = root
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
    return res


def in_order3(root):
    stack, res = [(root, False)], []
    while stack:
        cur, visited = stack.pop()
        if cur is None: continue
        if visited:
            res.append(cur.val)
        else:
            stack.append((cur.right, False))
            stack.append((cur, True))
            stack.append((cur.left, False))
    return res


def post_order1(root):
    if root is None: return []
    stack1, stack2, res = [root], [], []
    while stack1:
        cur = stack1.pop()
        stack2.append(cur)
        if cur.left:
            stack1.append(cur.left)
        if cur.right:
            stack1.append(cur.right)
    while stack2:
        res.append(stack2.pop().val)
    return res


def post_order2(root):
    if root is None: return []
    stack, res = [(root, False)], []
    while stack:
        cur, visited = stack.pop()
        if cur is None: continue
        if visited:
            res.append(cur.val)
        else:
            stack.append((cur, True))
            stack.append((cur.right, False))
            stack.append((cur.left, False))
    return res


if __name__ == '__main__':
    bst = BinaryTree(serialize=','.join(map(str, range(1, 1 << 5))))

    pre = bst.pre_order()
    assert pre == pre_order1(bst.root)
    assert pre == pre_order2(bst.root)
    assert pre == pre_order3(bst.root)
    assert pre == pre_order4(bst.root)

    in_ = bst.in_order()
    assert in_ == in_order1(bst.root)
    assert in_ == in_order2(bst.root)
    assert in_ == in_order3(bst.root)

    post = bst.post_order()
    assert post == post_order1(bst.root)
    assert post == post_order2(bst.root)
