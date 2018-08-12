__author__ = 'Hk4Fun'
__date__ = '2018/8/12 21:30'

import unittest
import sys

sys.path.append('..')
from union_find import QuickFind, QuickUnion, WQuickUnion, WQuickUnionWithPC


class TestUnionFind(unittest.TestCase):
    def setUp(self):
        self.fp = open('tinyUF.txt', 'r')
        self.n = int(self.fp.readline())

    def tearDown(self):
        self.fp.close()

    def _getpq(self):
        return map(int, self.fp.readline().split(' '))

    def _test(self, uf):
        for _ in range(self.n):
            uf.union(*self._getpq())
        self.assertEqual(uf.connected(0, 7), True)
        self.assertEqual(uf.connected(2, 3), False)
        self.assertEqual(uf.count(), 2)
        self.fp.seek(0, 0)
        self.fp.readline()

    def testQuickFind(self):
        self._test(QuickFind(self.n))

    def testQuickUnion(self):
        self._test(QuickUnion(self.n))

    def testWQuickUnion(self):
        self._test(WQuickUnion(self.n))

    def testWQuickUnionWithPC(self):
        self._test(WQuickUnionWithPC(self.n))


if __name__ == '__main__':
    unittest.main(verbosity=2)
