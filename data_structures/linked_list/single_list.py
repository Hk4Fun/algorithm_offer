__author__ = 'Hk4Fun'
__date__ = '2018/9/25 0:58'

from collections import Iterable


class Node:

    def __init__(self, val=None, next=None):
        self.val = val
        self._next = next

    def __repr__(self):
        return 'Node({!r})'.format(self.val)

    @property
    def next(self):
        return self._next


class SingleList:
    def __init__(self, iterable=None):
        self._dummyHead = Node()
        self._tail = None
        self._size = 0
        if iterable is not None and not isinstance(iterable, Iterable):
            raise TypeError("'{}' object is not iterable".format(type(iterable)))
        elif iterable is not None:
            self.extend(iterable)

    def __repr__(self):
        return 'SingleList([{}])'.format(','.join(map(lambda node: str(node.val), self)))

    def __str__(self):
        return 'SingleList({})'.format('->'.join(map(lambda node: str(node.val), self)))

    def __len__(self):
        return self._size

    def __getitem__(self, i):
        if isinstance(i, slice):
            start, end, step = i.indices(self._size)
            new_list = SingleList()
            if start >= self._size:
                return new_list
            cur = self._find_node_by_index(start)
            while cur and start < end:
                new_list.add_last(cur)
                for _ in range(step):
                    if cur:
                        cur = cur.next
                        start += 1
                    else:
                        break
            return new_list
        elif isinstance(i, int):
            if not -self._size <= i < self._size:
                raise IndexError('invalid index')
            if i == 0 or i == -self._size:
                return self.head
            if i == self._size - 1 or i == -1:
                return self.tail
            if i >= 0:
                return self._find_node_by_index(i)
            else:
                return self._find_node_by_index(self._size + i)
        else:
            raise TypeError('indices must be integers')

    def __setitem__(self, i, node):
        if not isinstance(node, Node):
            raise TypeError('item must be a Node')
        if not -self._size <= i < self._size:
            raise IndexError('invalid index')
        if i == 0 or i == -self._size:
            self._replace_head(node)
        elif i == self._size - 1 or i == -1:
            self._replace_tail(node)
        else:
            pre = self[i - 1]
            node._next = pre.next.next
            pre._next = node

    def __contains__(self, e):
        for node in self:
            if node.val == e:
                return True
        return False

    def __add__(self, other_list):
        if not isinstance(other_list, SingleList):
            raise TypeError('can only concatenate SingleList (not "{}") to SingleList'.format(type(other_list)))
        new_list = self.copy()
        new_list += other_list
        return new_list

    def __iadd__(self, other):
        if other is None:
            return self
        if isinstance(other, SingleList):
            if other.head is None:
                return self
            if self._tail is None:
                self._dummyHead._next = other.head
            else:
                self._tail._next = other.head
            self._tail = other.tail
            self._size += len(other)
        elif isinstance(other, Node):
            self.add_last(other)
        else:
            raise TypeError('can only concatenate SingleList or Node (not "{}") to SingleList'.format(type(other)))
        return self

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

    def __eq__(self, other):
        if not isinstance(other, SingleList):
            return False
        if len(other) != len(self):
            return False
        for i in range(len(self)):
            if self[i].val != other[i].val:
                return False
        return True

    @property
    def head(self):
        return self._dummyHead.next

    @property
    def tail(self):
        return self._tail

    def add_first(self, node):
        if not isinstance(node, Node):
            raise TypeError('node must be Node')
        node._next = self.head
        self._dummyHead._next = node
        self._size += 1
        if self._size == 1:
            self._tail = self._dummyHead.next

    def add_last(self, node):
        if not isinstance(node, Node):
            raise TypeError('node must be Node')
        if self._tail is None:
            self._dummyHead._next = node
        else:
            self._tail._next = node
        self._tail = node
        self._size += 1

    def insert(self, position, node, before=False):
        if not isinstance(node, Node):
            raise TypeError('param node should be a Node, not {}'.format(type(node)))
        if isinstance(position, int):  # insert node at index
            if not 0 <= position <= self._size:
                raise IndexError('invalid index')
            if position == 0:
                self.add_first(node)
                return
            if position == self._size:
                self.add_last(node)
                return
            pre = self._dummyHead
            for _ in range(position):
                pre = pre.next
            node._next = pre.next
            pre._next = node
        elif isinstance(position, Node):
            if before:  # insert node before position
                if position is self.head:
                    self.add_first(node)
                    return
                pre = self.previous(position)
                node._next = pre.next
                pre._next = node
            else:  # insert node after position
                if position is self.tail:
                    self.add_last(node)
                    return
                node._next = position.next
                position._next = node
        else:
            raise TypeError('position must be int or Node, not {}'.format(type(position)))
        self._size += 1

    def pop(self, i=None) -> Node:
        if i is None:
            i = self._size - 1
        if not 0 <= i < self._size:
            raise IndexError('pop index out of range')
        node = self[i]
        pre = self.previous(node)
        pre._next = node.next
        if i == self._size - 1:
            if pre is self._dummyHead:
                self._tail = None
            else:
                self._tail = pre
        self._size -= 1
        return node

    def remove(self, element_node):
        if element_node is None: return
        if isinstance(element_node, Node):
            node = element_node
        else:
            node = self.find_node_by_element(element_node)
            if node is None:
                raise ValueError('value not found')
        pre = self.previous(node)
        if pre is None:
            raise ValueError('node not found')
        pre._next = node.next
        self._size -= 1
        if node is self.tail:
            if pre is self._dummyHead:
                self._tail = None
            else:
                self._tail = pre

    def reverse(self):
        pre, cur = None, self.head
        self._tail = self.head
        while cur:
            cur._next, cur, pre = pre, cur.next, cur
        self._dummyHead._next = pre

    def previous(self, node):
        if node is None: return
        pre = self._dummyHead
        while pre and pre.next is not node:
            pre = pre.next
        return pre

    def extend(self, iterable):
        if not isinstance(iterable, Iterable):
            raise TypeError("'{}' object is not iterable".format(type(iterable)))
        for e in iterable:
            node = Node(e)
            self.add_last(node)

    def _find_node_by_index(self, i):
        if not 0 <= i < self._size:
            raise IndexError('invalid index')
        cur = self.head
        for _ in range(i):
            cur = cur.next
        return cur

    def find_node_by_element(self, e):
        cur = self.head
        while cur and cur.val != e:
            cur = cur.next
        return cur

    def index(self, element_node):
        if isinstance(element_node, Node):  # find index by node
            node = element_node
            for i, cur in enumerate(self):
                if cur is node:
                    return i
        else:  # find index by element
            e = element_node
            for i, node in enumerate(self):
                if node.val == e:
                    return i
        raise ValueError('{!r} not found'.format(element_node))

    def replace(self, position, node):
        if isinstance(position, int):
            self[position] = node
        elif isinstance(position, Node):
            if position is self.head:
                self._replace_head(node)
            elif position is self.tail:
                self._replace_tail(node)
            else:
                pre = self.previous(position)
                if pre is None:
                    raise ValueError('node not found')
                node._next = pre.next.next
                pre._next = node
        else:
            raise TypeError('position must int or Node, not {} '.format(type(position)))

    def copy(self):
        new_list = SingleList()
        for node in self:
            new_list.add_last(node)
        return new_list

    def _replace_head(self, node):
        if node is None: return
        node._next = self.head.next
        self._dummyHead._next = node

    def _replace_tail(self, node):
        if node is None: return
        pre = self.previous(self.tail)
        self._tail = pre._next = node
