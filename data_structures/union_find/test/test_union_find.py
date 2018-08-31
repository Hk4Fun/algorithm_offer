__author__ = 'Hk4Fun'
__date__ = '2018/8/12 21:30'

import unittest
import sys

sys.path.append('..')
from union_find import QuickFind, QuickUnion, WQuickUnion, WQuickUnionWithPC, DQuickUnion, DQuickUnionWithPC


class TestUnionFind(unittest.TestCase):
    def setUp(self):
        testfile = ('tinyUF.txt', 'mediumUF.txt')
        self.fps = [open(file, 'r') for file in testfile]
        self.ns = [int(fp.readline()) for fp in self.fps]

    def tearDown(self):
        for fp in self.fps:
            fp.close()

    def _getpq(self, fp):
        return map(int, fp.readline().split(' '))

    def _test(self, uf, fp, n):
        for _ in range(n):
            uf.union(*self._getpq(fp))
        if n == self.ns[0]:  # tinyUF.txt
            self.assertEqual(uf.connected(0, 7), True)
            self.assertEqual(uf.connected(2, 3), False)
            self.assertEqual(uf.count(), 2)
        elif n == self.ns[1]:  # mediumUF.txt
            self.assertEqual(uf.connected(43, 69), True)
            self.assertEqual(uf.connected(0, 7), False)
            self.assertEqual(uf.count(), 66)

    def testQuickFind(self):
        for fp, n in zip(self.fps, self.ns):
            self._test(QuickFind(n), fp, n)

    def testQuickUnion(self):
        for fp, n in zip(self.fps, self.ns):
            self._test(QuickUnion(n), fp, n)

    def testWQuickUnion(self):
        for fp, n in zip(self.fps, self.ns):
            self._test(WQuickUnion(n), fp, n)

    def testDQuickUnion(self):
        for fp, n in zip(self.fps, self.ns):
            self._test(DQuickUnion(n), fp, n)

    def testWQuickUnionWithPC(self):
        for fp, n in zip(self.fps, self.ns):
            self._test(WQuickUnionWithPC(n), fp, n)

    def testDQuickUnionWithPC(self):
        for fp, n in zip(self.fps, self.ns):
            self._test(DQuickUnionWithPC(n), fp, n)


if __name__ == '__main__':
    unittest.main(verbosity=2)
