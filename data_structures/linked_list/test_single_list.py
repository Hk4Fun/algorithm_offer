__author__ = 'Hk4Fun'
__date__ = '2018/9/25 13:24'

import pytest
from single_list import SingleList, Node


class TestSingleList:
    def test_repr_str(self):
        single_list = SingleList([1, 2, 3])
        assert single_list.__str__() == 'SingleList(1->2->3)'
        assert single_list.__repr__() == 'SingleList([1,2,3])'

        single_list = SingleList([])
        assert single_list.__str__() == 'SingleList()'
        assert single_list.__repr__() == 'SingleList([])'

        with pytest.raises(TypeError):
            tmp = SingleList(1)

    def test_len(self):
        single_list = SingleList([])
        assert len(single_list) == 0

        single_list = SingleList([1, 2, 3])
        assert len(single_list) == 3

        single_list.add_last(Node(0))
        assert len(single_list) == 4

        single_list.pop()
        assert len(single_list) == 3

    def test_getitem(self):
        single_list = SingleList([])
        with pytest.raises(IndexError):
            tmp = single_list[0]
        assert single_list[10:100:3] == SingleList([])

        single_list = SingleList([1, 2, 3])
        assert type(single_list[0]) is Node
        assert single_list[0].val == 1
        assert single_list[1].val == 2
        assert single_list[2].val == 3
        assert single_list[-1].val == 3
        assert single_list[-2].val == 2
        assert single_list[-3].val == 1
        assert type(single_list[-10:10]) is SingleList
        assert single_list[-10:10] == SingleList([1, 2, 3])
        assert type(single_list[0:1]) is SingleList
        assert single_list[0:1] == SingleList([1])
        assert single_list[1:3] == SingleList([2, 3])
        assert single_list[1:3:2] == SingleList([2])
        assert single_list[-10:10:2] == SingleList([1, 3])
        assert single_list[-10:10:3] == SingleList([1])
        assert single_list[10:100:3] == SingleList([])
        with pytest.raises(IndexError):
            tmp = single_list[-10].val
        with pytest.raises(IndexError):
            tmp = single_list[10].val
        with pytest.raises(TypeError):
            tmp = single_list[1.0].val

    def test_setitem(self):
        single_list = SingleList([])
        with pytest.raises(TypeError):
            single_list[0] = 0
        with pytest.raises(IndexError):
            single_list[0] = Node(0)

        single_list = SingleList([1, 2, 3])
        with pytest.raises(TypeError):
            single_list[0] = 0
        single_list[0] = Node(0)
        assert single_list == SingleList([0, 2, 3])
        single_list[1] = Node(1)
        assert single_list == SingleList([0, 1, 3])
        single_list[-1] = Node(-1)
        assert single_list == SingleList([0, 1, -1])
        single_list[-2] = Node(-2)
        assert single_list == SingleList([0, -2, -1])
        with pytest.raises(IndexError):
            single_list[-4] = Node(-4)
        with pytest.raises(IndexError):
            single_list[3] = Node(3)

    def test_contains(self):
        single_list = SingleList([])
        assert 0 not in single_list

        single_list = SingleList([1, 2, 3])
        assert 1 in single_list
        assert 2 in single_list
        assert 3 in single_list
        assert 4 not in single_list

    def test_add(self):
        assert SingleList([]) + SingleList([]) == SingleList([])
        assert SingleList([]) + SingleList([1]) == SingleList([1])
        assert SingleList([1]) + SingleList([2]) == SingleList([1, 2])
        single_list1 = SingleList([1])
        single_list2 = SingleList([2])
        single_list1 + single_list2
        assert single_list1 == SingleList([1])
        assert single_list2 == SingleList([2])

    def test_iadd(self):
        single_list = SingleList([])
        single_list += SingleList([])
        assert single_list == SingleList([])
        single_list += SingleList([1, 2, 3])
        assert single_list == SingleList([1, 2, 3])
        single_list += SingleList([])
        assert single_list == SingleList([1, 2, 3])
        single_list += SingleList([4])
        assert single_list == SingleList([1, 2, 3, 4])
        single_list += None
        assert single_list == SingleList([1, 2, 3, 4])
        single_list += Node(5)
        assert single_list == SingleList([1, 2, 3, 4, 5])
        single_list += Node()
        assert single_list == SingleList([1, 2, 3, 4, 5, None])

    def test_iter(self):
        single_list = SingleList([])
        assert list(single_list) == []

        single_list = SingleList([1, 2, 3])
        assert [node.val for node in single_list] == [1, 2, 3]

        it = iter(single_list)
        assert next(it).val == 1
        assert next(it).val == 2
        assert next(it).val == 3
        with pytest.raises(StopIteration):
            next(it)
        with pytest.raises(StopIteration):
            next(it)
        it = iter(single_list)
        assert next(it).val == 1

    def test_eq(self):
        assert SingleList([]) == SingleList([])
        assert SingleList([1, 2, 3]) == SingleList([1, 2, 3])
        assert SingleList([]) != SingleList([1])

    def test_head_tail(self):
        single_list = SingleList([])
        assert single_list.head is None
        assert single_list.tail is None
        node1 = Node(1)
        single_list.add_last(node1)
        assert single_list.head is node1
        assert single_list.tail is node1
        single_list.pop()
        assert single_list.head is None
        assert single_list.tail is None
        node2 = Node(2)
        single_list.add_first(node1)
        single_list.add_last(node2)
        assert single_list.head is node1
        assert single_list.tail is node2
        single_list = SingleList([1, 2, 3])
        assert single_list.head.val is 1
        assert single_list.tail.val is 3
        single_list += SingleList([4, 5, 6])
        assert single_list.head.val is 1
        assert single_list.tail.val is 6
        single_list += SingleList([])
        assert single_list.head.val is 1
        assert single_list.tail.val is 6

    def test_add_first(self):
        single_list = SingleList([])
        with pytest.raises(TypeError):
            single_list.add_first(1)
        single_list.add_first(Node(1))
        assert single_list == SingleList([1])
        single_list.add_first(Node(2))
        assert single_list == SingleList([2, 1])
        assert len(single_list) == 2

    def test_add_last(self):
        single_list = SingleList([])
        with pytest.raises(TypeError):
            single_list.add_last(1)
        single_list.add_last(Node(1))
        assert single_list == SingleList([1])
        single_list.add_last(Node(2))
        assert single_list == SingleList([1, 2])
        assert len(single_list) == 2

    def test_insert(self):
        single_list = SingleList([])
        with pytest.raises(IndexError):
            single_list.insert(-1, Node(1))
        with pytest.raises(IndexError):
            single_list.insert(1, Node(1))
        with pytest.raises(TypeError):
            single_list.insert(-1, 1)
        single_list.insert(0, Node(1))
        assert single_list == SingleList([1])
        single_list.insert(0, Node(2))
        assert single_list == SingleList([2, 1])
        single_list.insert(1, Node(3))
        assert single_list == SingleList([2, 3, 1])
        single_list.insert(3, Node(4))
        assert single_list == SingleList([2, 3, 1, 4])
        assert single_list.head.val == 2
        assert single_list.tail.val == 4
        assert len(single_list) == 4

        single_list = SingleList([1])
        single_list.insert(single_list.head, Node(2))
        assert single_list == SingleList([1, 2])
        single_list.insert(single_list.head, Node(3), before=True)
        assert single_list == SingleList([3, 1, 2])
        single_list.insert(single_list.tail, Node(4))
        assert single_list == SingleList([3, 1, 2, 4])
        single_list.insert(single_list.tail, Node(5), before=True)
        assert single_list == SingleList([3, 1, 2, 5, 4])
        single_list.insert(single_list[2], Node(6))
        assert single_list == SingleList([3, 1, 2, 6, 5, 4])
        single_list.insert(single_list[2], Node(7), before=True)
        assert single_list == SingleList([3, 1, 7, 2, 6, 5, 4])
        assert single_list.head.val == 3
        assert single_list.tail.val == 4
        assert len(single_list) == 7

    def test_pop(self):
        single_list = SingleList([])
        with pytest.raises(IndexError):
            single_list.pop()
        single_list = SingleList([1, 2, 3])
        with pytest.raises(IndexError):
            single_list.pop(3)
        with pytest.raises(IndexError):
            single_list.pop(-1)
        assert single_list.pop().val == 3
        assert single_list.pop(0).val == 1
        assert single_list.tail.val == 2
        assert single_list.head.val == 2
        assert len(single_list) == 1
        assert single_list.pop().val == 2
        assert single_list.tail == None
        assert single_list.head == None
        assert len(single_list) == 0
        single_list = SingleList([1, 2, 3])
        assert single_list.pop(1).val == 2
        assert single_list.tail.val == 3
        assert single_list.head.val == 1
        assert len(single_list) == 2

    def test_remove(self):
        single_list = SingleList([])
        with pytest.raises(ValueError):
            single_list.remove(0)
        single_list.remove(single_list.head)
        assert single_list.tail is None
        assert single_list.head is None
        assert len(single_list) == 0
        assert single_list == SingleList([])

        single_list = SingleList([1, 2, 3])
        single_list.remove(1)
        assert single_list == SingleList([2, 3])
        single_list.remove(3)
        assert single_list == SingleList([2])
        assert single_list.tail.val == 2
        assert single_list.head.val == 2
        assert len(single_list) == 1
        with pytest.raises(ValueError):
            single_list.remove(3)
        single_list.remove(2)
        assert single_list.tail is None
        assert single_list.head is None
        assert len(single_list) == 0

        single_list = SingleList([1, 2, 3])
        single_list.remove(single_list.head)
        assert single_list == SingleList([2, 3])
        assert single_list.tail.val == 3
        assert single_list.head.val == 2
        assert len(single_list) == 2
        single_list.remove(single_list.tail)
        assert single_list == SingleList([2])
        assert single_list.tail.val == 2
        assert single_list.head.val == 2
        assert len(single_list) == 1
        with pytest.raises(ValueError):
            single_list.remove(Node(1))

        single_list = SingleList([1, 2, 3])
        single_list.remove(single_list[1])
        assert single_list.tail.val == 3
        assert single_list.head.val == 1
        assert len(single_list) == 2

    def test_reverse(self):
        single_list = SingleList([])
        single_list.reverse()
        assert single_list == SingleList([])

        single_list = SingleList([1])
        single_list.reverse()
        assert single_list == SingleList([1])

        single_list = SingleList([1, 2, 3])
        single_list.reverse()
        assert single_list == SingleList([3, 2, 1])
        assert single_list.head.val == 3
        assert single_list.tail.val == 1
        assert len(single_list) == 3

    def test_previous(self):
        single_list = SingleList([])
        assert single_list.previous(single_list.head) is None
        assert single_list.previous(single_list.tail) is None
        assert single_list.previous(Node()) is None

        single_list = SingleList([1, 2, 3])
        assert single_list.previous(single_list.head) is single_list._dummyHead
        assert single_list.previous(single_list.tail).val == 2
        assert single_list.previous(Node(2)) is None
        assert single_list.previous(None) is None
        assert single_list.previous(single_list[1]).val == 1

    def test_extend(self):
        single_list = SingleList([])
        single_list.extend([])
        assert single_list == SingleList([])
        with pytest.raises(TypeError):
            single_list.extend(1)
        single_list.extend([0])
        assert single_list == SingleList([0])
        single_list.extend([1, 2, 3])
        assert single_list == SingleList([0, 1, 2, 3])
        assert single_list.tail.val == 3
        assert single_list.head.val == 0
        assert len(single_list) == 4
        tmp_list = SingleList([0, 1, 2, 3])
        single_list.extend(tmp_list)
        assert single_list.tail.val is tmp_list[-1]
        assert single_list.head.val == 0
        assert len(single_list) == 8

    def test_find_node_by_element(self):
        single_list = SingleList([])
        assert single_list.find_node_by_element(0) is None

        single_list = SingleList([1, 2, 3, 2, 3])
        assert single_list.find_node_by_element(0) is None
        assert single_list.find_node_by_element(1) is single_list[0]
        assert single_list.find_node_by_element(2) is single_list[1]
        assert single_list.find_node_by_element(3) is single_list[2]

    def test_index(self):
        single_list = SingleList([])
        with pytest.raises(ValueError):
            single_list.index(0)
        with pytest.raises(ValueError):
            single_list.index(Node())
        with pytest.raises(ValueError):
            single_list.index(single_list.head)
        with pytest.raises(ValueError):
            single_list.index(single_list.tail)

        single_list = SingleList([1, 2, 3])
        assert single_list.index(1) == 0
        assert single_list.index(2) == 1
        assert single_list.index(3) == 2
        assert single_list.index(single_list[0]) == 0
        assert single_list.index(single_list[1]) == 1
        assert single_list.index(single_list[2]) == 2
        assert single_list.index(single_list.head) == 0
        assert single_list.index(single_list.tail) == len(single_list) - 1

    def test_replace(self):
        single_list = SingleList([])
        with pytest.raises(IndexError):
            single_list.replace(0, Node())
        with pytest.raises(TypeError):
            single_list.replace(single_list.tail, Node())

        single_list = SingleList([1, 2, 3])
        node1 = Node(2)
        single_list.replace(0, node1)
        assert single_list.head is node1
        assert single_list == SingleList([2, 2, 3])
        node2 = Node(4)
        single_list.replace(single_list.tail, node2)
        assert single_list.tail is node2
        assert single_list == SingleList([2, 2, 4])
        node3 = Node(5)
        single_list.replace(1, node3)
        assert single_list[1] is node3
        assert single_list == SingleList([2, 5, 4])
        with pytest.raises(ValueError):
            single_list.replace(Node(), Node(6))

    def test_copy(self):
        single_list = SingleList([])
        assert single_list.copy() == SingleList([])

        single_list = SingleList([1])
        assert single_list.copy() == SingleList([1])

        single_list = SingleList([1, 2, 3])
        assert single_list.copy() == SingleList([1, 2, 3])
