from HeapSort import heapSort, swap, buildMaxHeap, sifDown
import unittest

class TestHeaSort(unittest.TestCase):
    def test_1(self):
        self.assertEqual(heapSort([7, 5, 10, 1, 4, 9, 6, 8, 2, 3]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == '__main__':
  unittest.main()
